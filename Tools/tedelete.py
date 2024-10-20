File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\fastapi\routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\fastapi\routing.py", line 212, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mawaf\HackathonSFverticalagent\app.py", line 23, in run_agent_endpoint
    resp = main_(query)
           ^^^^^^^^^^^^
  File "C:\Users\mawaf\HackathonSFverticalagent\main.py", line 70, in main_
    result = run_agent(query,chat_history)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mawaf\HackathonSFverticalagent\main.py", line 59, in run_agent
    result = agent_executor.invoke({"input": query, "chat_history": chat_history})
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\langchain\chains\base.py", line 170, in invoke
    raise e
  File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\langchain\chains\base.py", line 160, in invoke
    self._call(inputs, run_manager=run_manager)
  File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\langchain\agents\agent.py", line 1629, in _call
    next_step_output = self._take_next_step(
                       ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\langchain\agents\agent.py", line 1335, in _take_next_step
    [
  File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\langchain\agents\agent.py", line 1335, in <listcomp>
    [
  File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\langchain\agents\agent.py", line 1420, in _iter_next_step
    yield self._perform_agent_action(
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\langchain\agents\agent.py", line 1442, in _perform_agent_action      
    observation = tool.run(
                  ^^^^^^^^^
  File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\langchain_core\tools\base.py", line 689, in run
    raise error_to_raise
  File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\langchain_core\tools\base.py", line 657, in run
    response = context.run(self._run, *tool_args, **tool_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mawaf\HackathonSFverticalagent\.venv\Lib\site-packages\langchain_core\tools\structured.py", line 80, in _run
    return self.func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mawaf\HackathonSFverticalagent\Tools\linkedin_axon.py", line 49, in send_linkedin_msg
    if not conversationId:
           ^^^^^^^^^^^^^^
UnboundLocalError: cannot access local variable 'conversationId' where it is not associated with a value