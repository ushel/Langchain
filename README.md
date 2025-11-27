tavily is most popular choice for integrating websearch into an agent 

model dose not execute the tool itself, it only produces the argument for tool call

system running langchain will execute the tool and propogate back the output to the model

how the llm know how tool to you and when to call tool.

usually tool description given in the tool will tell llm what the tool is doing so it will know when to use it.

and in that llm call we will also provide what arguments does the call receive(name, arguments).