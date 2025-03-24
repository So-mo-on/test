{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0a5c51d8-0e4e-4bd6-8f69-a28c8da37a26",
   "metadata": {},
   "outputs": [],
   "source": [
    "# pip install streamlit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8fa86d97-d96e-4388-bbd6-b881679d78ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-03-23 22:22:42.670 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.728 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /Users/fatemehsoleymanimoghadam/Library/Python/3.9/lib/python/site-packages/ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-03-23 22:22:42.728 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.728 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.728 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.729 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.729 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.729 Session state does not function when running a script without `streamlit run`\n",
      "2025-03-23 22:22:42.729 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.729 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.729 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.730 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.730 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.730 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 22:22:42.730 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "# Your function\n",
    "def my_function(user_input):\n",
    "    return f\"Hello, {user_input}!\"\n",
    "\n",
    "# Streamlit App\n",
    "st.title(\"My Python Web App\")\n",
    "user_input = st.text_input(\"Enter your name:\")\n",
    "if st.button(\"Submit\"):\n",
    "    result = my_function(user_input)\n",
    "    st.success(result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "442daa66-bcdf-40da-8d5d-6c0f50eeeb8d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
