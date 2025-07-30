import os
import re
import csv
from pathlib import Path

# Directory containing the By_District markdown files
BY_DISTRICT_DIR = Path("c:/Users/Shama/OneDrive/Documents/Course_Materials/CPT-236/Projects/MarginofVictory/NCRealignment/nc-election-analysis/data/Congressional_Data/By_District")

# More robust regex: allow extra/missing spaces, decimals, and tolerate missing trailing zeros
TREND_LINE_RE = re.compile(
    r"^(\s*-\s*\d{4}(?:\.\d+)?):\s*"  # year prefix
    r"([^\(]+)\(([^\)]+)\)\s*vs\.\s*([^\(]+)\(([^\)]+)\):\s*"  # candidate 1 vs candidate 2
    r"([^\(]+)\(([^\)]+)\)\s*([+\-]?[\d\.]+)\s*"  # winner (party) margin
    r"\((\d{1,3}(?:\.\d+)?)% to (\d{1,3}(?:\.\d+)?)%\)"
)

CANDIDATES = {
    'President': {
        2008: ('Obama (D)', 'McCain (R)'),
        2012: ('Obama (D)', 'Romney (R)'),
        2016: ('Clinton (D)', 'Trump (R)'),
        2020: ('Biden (D)', 'Trump (R)'),
        2024: ('Harris (D)', 'Trump (R)'),
    },
    'Governor': {
        2008: ('Perdue (D)', 'McCrory (R)'),
        2012: ('Dalton (D)', 'McCrory (R)'),
        2016: ('Cooper (D)', 'McCrory (R)'),
        2020: ('Cooper (D)', 'Forest (R)'),
        2024: ('Stein (D)', 'Robinson (R)'),
    },
    'Senate': {
        2008: ('Hagan (D)', 'Dole (R)'),
        2010: ('Marshall (D)', 'Burr (R)'),
        2014: ('Hagan (D)', 'Tillis (R)'),
        2016: ('Ross (D)', 'Burr (R)'),
        2020: ('Cunningham (D)', 'Tillis (R)'),
        2022: ('Beasley (D)', 'Budd (R)'),
    },
    'Attorney General': {
        2016: ('Stein (D)', 'Newton (R)'),
        2020: ('Stein (D)', "O'Neill (R)"),
        2024: ('Jackson (D)', 'Bishop (R)'),
    },
    'Lt Governor': {
        2016: ('Coleman (D)', 'Forest (R)'),
        2020: ('Holley (D)', 'Robinson (R)'),
        2024: ('Hunt (D)', 'Weatherman (R)'),
    },
    'Supreme Court': {
        2022: ('Inman (D)', 'Dietz (R)'),
        2022.1: ('Ervin (D)', 'Allen (R)'),
        2024: ('Riggs (D)', 'Griffin (R)'),
    },
}

def parse_float(s):
    try:
        return float(s)
    except Exception:
        return None

def fix_trend_line(line):
    m = TREND_LINE_RE.match(line)
    if not m:
        return line  # Not a trend line
    prefix, cand1, party1, cand2, party2, winner, winner_party, margin, pct1, pct2 = m.groups()
    cand1 = cand1.strip(); party1 = party1.strip()
    cand2 = cand2.strip(); party2 = party2.strip()
    pct1f = parse_float(pct1)
    pct2f = parse_float(pct2)
    if pct1f is None or pct2f is None:
        return line
    # Always determine winner/loser by percentage
    if pct1f > pct2f:
        actual_winner = (cand1, party1, pct1f)
        actual_loser = (cand2, party2, pct2f)
    else:
        actual_winner = (cand2, party2, pct2f)
        actual_loser = (cand1, party1, pct1f)
    correct_margin = round(actual_winner[2] - actual_loser[2], 2)
    # Format sign
    sign = "+" if correct_margin >= 0 else "-"
    correct_margin_str = f"{sign}{abs(correct_margin):.2f}".rstrip("0").rstrip(".")
    # Compose new line, always winner first
    new_line = (
        f"{prefix}: {actual_winner[0]} ({actual_winner[1]}) vs. {actual_loser[0]} ({actual_loser[1]}): "
        f"{actual_winner[0]} ({actual_winner[1]}) {correct_margin_str} "
        f"({actual_winner[2]:.2f}% to {actual_loser[2]:.2f}%)"
    )
    return new_line

def get_csv_filename(year, race):
    # Map markdown section/race to CSV filename
    # e.g., 2016, Senate -> '2016 Senate.csv'
    return f"{year} {race}.csv"

def get_csv_row(csv_path, district_id):
    # Return the row for the given district (as string, e.g., '1')
    with open(csv_path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['ID'].strip().replace('"','') == str(district_id):
                return row
    return None

def fix_trend_line_with_csv(line, year, race, district_id):
    # Use candidate names from CANDIDATES if available
    try:
        year_key = int(year) if race != 'Supreme Court' or '.' not in year else float(year)
    except Exception:
        year_key = int(year)
    cand_names = CANDIDATES.get(race, {}).get(year_key, ("Dem (D)", "Rep (R)"))
    dem_name, rep_name = cand_names
    csv_name = get_csv_filename(year, race)
    csv_path = Path(BY_DISTRICT_DIR.parent / csv_name)
    if not csv_path.exists():
        return line  # CSV missing, skip
    row = get_csv_row(csv_path, district_id)
    if not row:
        return line  # District missing in CSV
    try:
        dem = float(row['Dem']) * 100
        rep = float(row['Rep']) * 100
    except Exception:
        return line
    # Always pair dem_name with dem, rep_name with rep, then sort by percentage
    candidate_percents = [
        (dem_name, dem),
        (rep_name, rep)
    ]
    candidate_percents.sort(key=lambda x: x[1], reverse=True)
    winner, winner_pct = candidate_percents[0]
    loser, loser_pct = candidate_percents[1]
    margin = round(winner_pct - loser_pct, 2)
    sign = '+' if margin >= 0 else '-'
    margin_str = f"{sign}{abs(margin):.2f}".rstrip('0').rstrip('.')
    # Compose new line
    new_line = (
        f"    - {year}: {winner} vs. {loser}: {winner} {margin_str} "
        f"({winner_pct:.2f}% to {loser_pct:.2f}%)"
    )
    return new_line
def remove_extra_blank_lines(lines):
    new_lines = []
    blank = False
    for line in lines:
        if line.strip() == '':
            if not blank:
                new_lines.append(line)
            blank = True
        else:
            new_lines.append(line)
            blank = False
    return new_lines

def process_file(path):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    new_lines = []
    current_race = None
    for idx, line in enumerate(lines):
        # Detect section (e.g., '- **Senate:**')
        section_match = re.match(r"\s*- \*\*(.+?):\*\*", line)
        if section_match:
            current_race = section_match.group(1).strip()
        # Detect trend line
        m = TREND_LINE_RE.match(line)
        if m and current_race:
            # Extract year and district from line and filename
            prefix = m.group(1)
            year_match = re.search(r'(\d{4})', prefix)
            if year_match:
                year = year_match.group(1)
                # Get district from filename (e.g., NC_1_trends.md)
                district_match = re.search(r'NC_(\d+)_trends', str(path))
                if district_match:
                    district_id = district_match.group(1)
                    new_lines.append(fix_trend_line_with_csv(line, year, current_race, district_id))
                    continue
        # Default: keep line as is
        new_lines.append(line.rstrip("\n"))
    # Remove extra blank lines for compactness
    compact_lines = remove_extra_blank_lines([l + "\n" for l in new_lines])
    # Only write if changed
    if [l + "\n" for l in lines] != compact_lines:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(compact_lines)
        print(f"Updated: {path}")
    else:
        print(f"No changes: {path}")

def check_candidate_mapping():
    print("Checking CANDIDATES mapping for (D) first, (R) second...")
    for race, years in CANDIDATES.items():
        for year, names in years.items():
            if len(names) != 2:
                print(f"  [ERROR] {race} {year}: mapping does not have exactly 2 candidates: {names}")
                continue
            dem_name, rep_name = names
            if '(D)' not in dem_name or '(R)' not in rep_name:
                print(f"  [WARNING] {race} {year}: mapping may be reversed or missing party: {names}")

def main():
    for i in range(1, 15):
        fname = f"NC_{i}_trends.md"
        fpath = BY_DISTRICT_DIR / fname
        if fpath.exists():
            process_file(fpath)
        else:
            print(f"Missing: {fpath}")

if __name__ == "__main__":
    check_candidate_mapping()
    main()
