# connection_live_ping
A simple python scripts that tells you when your internet died

# Requirements
<ul>
  <li>All the libraries listed in the requirements.txt file installed</li>
  <li>(Optional) Compile it before running (use auto-py-to-exe with the window-based compiling and include the 2 icons before exporting)</li>
</ul>

# How it works ?
<ol>
  <li>It calls test_connection() function which ping https://www.google.com and return true if ok</li>
  <li><ul>
    <li>If returned false in the first time, the program will exit with connectivity error.</li>
    <li>If returned true in the first time, the same process will repeat every 30 seconds</li></ul>
  <li>If at any moment the program failed to ping the google website, it will exit with connectivity error.</li>
</ol>

# What is the purpose of this script ?
It will save you time by telling when your connection died instead of getting of your seet for checking the modem or the phone hotspot
