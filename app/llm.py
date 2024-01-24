from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

class LanguageModel:

    def __init__(self):
        load_dotenv()

        self.llm = ChatGoogleGenerativeAI(model="gemini-pro")
        
    def parseInput(self, date: str, command: str) -> str:

        inputTemplate = """Interpret the details from the following natural language command to create either an event or assignment for a school-productivity application. 
        Analyze the text to extract the necessary information. Provide a structured format of the details mentioned. 
        If a detail is too vague or unspecified, state it as UNSPECIFIED.
        For the type, an event will typically be quizzes, tests, presentations. Assignments will more often be things or actions due.
        For the title, try to keep it short and concise and push specifics to the description.
        For the date (and end date if exists), ensure it is in RFC3339 format (ex. 2020-06-18T17:24:53Z)
        If the command itself isn't comprehendable or doesn't make sense, state the Type to NONE.
        Do not deviate in the slightest from this expected format in your result.

        Expected format:
        Type: [Event or Assignment or NONE]
        Title: [Event/Assignment title or UNSPECIFIED]
        Description: [Event/Assignment description or UNSPECIFIED]
        Date: [Event/Assignment date in RFC3339 format or UNSPECIFIED]
        End date: [End date for multiple day events in RFC339 format or UNSPECIFIED]

        Do not deviate from this structure at all.
        For reference, today is {date}.
        Provide a structured output based on these guidelines for the following inputted command:

        {command}"""
        inputPrompt = PromptTemplate.from_template(inputTemplate)

        self.chain = inputPrompt | self.llm
        result = self.chain.invoke({'command': command, 'date': date})

        return result.content
