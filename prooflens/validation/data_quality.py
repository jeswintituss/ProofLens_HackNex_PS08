def inspect_dataframe(df):
    report = []
    duplicates = int(df.duplicated().sum())
    missing = int(df.isna().sum().sum())

    report.append({
        "severity": "warning" if duplicates else "info",
        "message": f"⚠ {duplicates} duplicate row(s) detected." if duplicates else "✓ No completely duplicated rows detected."
    })
    report.append({
        "severity": "warning" if missing else "info",
        "message": f"⚠ {missing} missing cell(s) detected." if missing else "✓ No missing cells detected."
    })
    report.append({
        "severity": "info",
        "message": f"✓ Dataset contains {len(df)} rows and {len(df.columns)} columns."
    })
    return report
