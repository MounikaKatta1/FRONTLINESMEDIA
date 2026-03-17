from helper import get_completion

prompt = """
Summarize the below paragraph in 5 Bullet points:

The future of business is being shaped by AI and intelligent agents. We envision billions of AI agents working alongside humans, fundamentally changing how organizations operate and innovate. Whether you're just starting with AI or ready to scale, AWS provides the flexibility to choose your path while maintaining control of your data and costs. AWS is helping companies and builders move beyond prompts and POCs to reimagine how work gets done with agentic AI—turning ideas into agents, code into capability, and effort into measurable impact. Choose AWS to get the freedom to invent your way, maximize value of every AI investment, and build confidently with AI you can trust.
"""

result = get_completion(prompt)
print(result) 