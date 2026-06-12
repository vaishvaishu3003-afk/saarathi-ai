def sarathi_ai(query):
    query = query.lower()

    if "python" in query:
        return """
🐍 Python Developer Roadmap

1. Learn Python fundamentals
2. Practice OOP concepts
3. Learn Git & GitHub
4. Build mini projects
5. Learn Flask/Streamlit
6. Deploy projects online
"""

    elif "placement" in query:
        return """
💼 Placement Preparation Plan

1. Practice DSA daily
2. Improve aptitude skills
3. Build strong projects
4. Create a professional resume
5. Attend mock interviews
"""

    elif "hackathon" in query:
        return """
🏆 Hackathon Success Guide

1. Identify a real-world problem
2. Build an MVP first
3. Focus on deployment
4. Prepare a clear demo
5. Explain impact and future scope
"""

    else:
        return f"""
🧭 Sarathi AI Guidance

Topic: {query}

1. Understand the fundamentals
2. Create a learning roadmap
3. Build practical projects
4. Practice consistently
5. Showcase your work

🚀 Success comes from continuous learning.
"""