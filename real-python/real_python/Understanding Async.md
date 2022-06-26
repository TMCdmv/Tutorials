### Understanding Asynchronous Programming
A **synchronous program** is executed one step at a time. Even with conditional branching, loops and function calls, you can still think about the code in terms of taking one execution step at a time. When each step is complete, the program moves on to the next one.  
Here are two examples of programs that work this way:  
- **Batch processing programs** are often created as synchronous programs. You get some input, process it, and create some output. Steps follow one after the other until the program reaches the desired output. The program only needs to pay attention to the steps and their order.  
- **Command-line programs** are small, quick processes that run in a terminal. These scripts are used to create something, transform one thing into something else, generate a report, or perhaps list out some data. This can be expressed as a series of program steps that are executed sequentially until the program is done.  

An **asynchronous program** behaves differently. It still takes one execution step at a time. The difference is that the system may not wait for an execution step to be completed before moving on to the next one.  

This means that the program will move on to future execution steps even though a previous step hasn’t yet finished and is still running elsewhere. This also means that the program knows what to do when a previous step does finish running.  

Why would you want to write a program in this manner? The rest of this article will help you answer that question and give you the tools you need to elegantly solve interesting asynchronous problems.

#### Building a Synchronous Web Server  
A web server’s basic unit of work is, more or less, the same as batch processing. The server will get some input, process it, and create the output. Written as a synchronous program, this would create a working web server.A web server’s basic unit of work is, more or less, the same as batch processing. The server will get some input, process it, and create the output. Written as a synchronous program, this would create a working web server.  

It would also be an absolutely terrible web server.  

Why? In this case, one unit of work (input, process, output) is not the only purpose. The real purpose is to handle hundreds or even thousands of units of work as quickly as possible. This can happen over long periods of time, and several work units may even arrive all at once.