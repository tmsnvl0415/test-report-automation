# scripts/generate_report.py

import json
import pandas as pd
from datetime import datetime
from pathlib import Path

# 경로 설정
report_path = Path("report/report.json")
output_path = Path("report/Test_Report.xlsx")

# JSON 읽기
with report_path.open() as f:
    data = json.load(f)

# 테스트 결과 정리
results = []
for test in data.get("tests", []):
    results.append({
        "Test Name": test["nodeid"],
        "Result": test["outcome"],
        "Duration (s)": round(test["duration"], 3)
    })

df = pd.DataFrame(results)

# 요약
summary = {
    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Total": len(df),
    "Passed": (df["Result"] == "passed").sum(),
    "Failed": (df["Result"] == "failed").sum(),
    "Skipped": (df["Result"] == "skipped").sum()
}
summary_df = pd.DataFrame([summary])

# Excel 저장
with pd.ExcelWriter(output_path) as writer:
    df.to_excel(writer, sheet_name="Details", index=False)
    summary_df.to_excel(writer, sheet_name="Summary", index=False)

print(f"? Report saved to {output_path}")
