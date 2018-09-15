This directory will be touching postmortem
=============================================

Issue Summary:

The issue started on Saturday, 15 Sep 2018 17:44:52 GMT and ended on Saturday, 15 Sep 2018 18:11:20 GMT
Acting as a Client to see what we experiencing on the client side, with an attempt of running curl -sI 127.0.0.1 into a given container I noticed I received a "HTTP/1.0 500 Internal Server Error" from the "Server: Apache/2.4.7 (Ubuntu)".
26% of users were affected in downtime since 26% of web users use wordpress)
I kept noticing that I kept getting errors about having "No such file of directory". The root cause of this issue was there was a typo within some of the file names when running curl -sI 127.0.0.1.

 lstat("/var/www/html/wp-includes/class-wp-locale.phpp"

Timeline:

The issue was detected on Saturday, 15 Sep 2018 17:44:52 GMT

This issue was discovered by Germo, our student software engineer when she tried to perform a curl on a container that was given to her by a previous user.

Actions and debugging paths that were taken:

Saturday, 15 Sep 2018 17:48:32 GMT - Run (ps auxf): So I can show processes for all users, display the owner's of the process, along with the processes not attached to the terminal. The error was coming from user "www-data" which was the Apache2 web server.

Saturday, 15 Sep 2018 17:50:02 GMT - Run (strace -p "Input Apache2 pid"): so you can detect what issues were for that specific pid. I received "Process 43 attached accept4(4," .

Saturday, 15 Sep 2018 17:52:08 GMT - In another window I decided to curl 127.0.0.1 once again then I received I noticed errors about having "No such file or directory".
lstat("/var/www/html/wp-includes/class-wp-locale.phpp".

From this point on the issue, was obvious. There were spelling errors within the filename, they meant to type php not phpp.

Saturday, 15 Sep 2018 18:11:20 GMT - No need to escalate the situation since Germo had it under control.

Root cause and resolution:

The root cause of the 500 Internal Error was due to a simple typo ("phpp" instead of "php") that I found within their php files which left us with an unresponsive web server.

I had to create a puppet file named 0-strace_is_your_friend.pp that contains

exec {'/var/www/html/wp-setting.php':

path => ['/bin'],

command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",}.

The command above can easily just replace those files that have "class-wp-local.phpp" with "class-wp-local.php".

Corrective and preventative:

Things that can be done so this issue doesn't occur is make pull request with an explanation what and why do you what you do.

Things we need to do:

- Add monitoring for our web servers so if there is downtime and there is an error we can get notified
- Make pull requests a standard