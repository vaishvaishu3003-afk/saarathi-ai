def sarathi_ai(query, lang="en", context=""):
    query = query.lower()

    if "python" in query:
        return """
🐍 Python Developer Roadmap

1. Learn Python fundamentals
2. Practice OOP concepts
3. Learn Git & GitHub
4. Build projects
5. Learn frameworks
"""

    elif "placement" in query:
        return """
💼 Placement Preparation Plan

1. Practice DSA
2. Improve aptitude
3. Build projects
4. Resume preparation
"""

    elif "hackathon" in query:
        return """
🏆 Hackathon Guide

1. Pick problem
2. Build MVP
3. Deploy fast
4. Present clearly
"""

    else:
        return f"""
🧭 Sarathi AI Response

Topic: {query}

Context: {context[:200] if context else "No document"}

1. Learn basics
2. Practice daily
3. Build projects
4. Stay consistent
"""
