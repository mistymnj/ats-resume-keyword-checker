skills = ["python", "sql", "flask", "html", "css", "ai", "machine learning", "git"]

job_desc = input("Paste Job Description: ").lower()
resume = input("Paste Your Resume: ").lower()

found = [s for s in skills if s in resume]
missing = [s for s in skills if s in resume and s not in job_desc] # fix this logic
print(f"Found: {found}")
print(f"Missing: {missing}")
print(f"Match: {len(found)/len(skills)*100}%")