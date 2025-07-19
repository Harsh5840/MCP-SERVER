from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# TODO: Write a tool to read a doc

@mcp.tool(
    name="read_the_doc",
    description="Read the content of the given document"
)

def read_doc(
    doc_id:str = Field(description="id of the document to be checked")
):
    if doc_id not in docs:
        raise ValueError(f"Doc id {doc_id} not found in original doc")
    return docs[doc_id]
    
# TODO: Write a tool to edit a doc

@mcp.tool(
    name="edit_the_doc",
    description="Edit the content of the given document"
)
def edit_doc(
    doc_id:str = Field(description="id of the document to be edited"),
    old_content:str = Field(description="old content of the document"), 
    new_content:str = Field(description="new content of the document")
):
    if doc_id not in docs:
        raise ValueError(f"Doc id {doc_id} not found in original doc")
    docs[doc_id] = docs[doc_id].replace(old_content, new_content)
    return docs[doc_id]
# TODO: Write a resource to return all doc id's
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")  #this line means that the server will run on the console , transport can be "stdio" or "grpc" , stdio means that the server will run on the console and grpc means that the server will run on a grpc server
