# Langchain

1. create new branch 

git checkout --orphan project/hello-world

git rm -rf . to remove files from this directory (branch)

use uv package manager

uv add langchain --dev

uv add langchain-openai

black . (to format the code)

isort .



What are AI agents: -

Agent ~= control flow defined by an LLM

start -> step 1 -> LLM -> step2 - end
           |<-------|

chain developer defined control flow

start -> step1 -> step 2 -> end


agent -> equip LLM with tools

llm

toolkit
tool
tool

ReAct Agent Architecture

                        |----action---->Tool 
query -> thinking (LLM) |<--- observation-|
                        |----Finish---->Answer



langChain ReAct Agent -----------> Tool Calling Agent -----------> LangGraph ReAct Agent -------------> LangChain create_agent() (v1.0)
        ^                                  ^                                  ^                                    ^
        |                                  |                                  |                                    |
        |                                  |                                  |                                    |
        |                                  |                                  |                                    |
    ReAct Prompt                     Function calling                  Function calling                     LangGraph ReActAgent



