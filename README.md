# CIS-106-Jess-Harkness

## Assignment 1

In 2020, I graduated from the University of Vermont with a B.S. in animal science and a minor in wildlife biology. I have been working in the general realm of conservation biology since graduating, mostly doing fieldwork jobs. I have recently decided that I want to pivot my career trajectory into GIS, which is an increasingly important tool used in conservation work. I enrolled in Harper's GIS Certificate program in June and chose to take this course (CIS 106) as my elective for the program. Familiarity with computer programming is an in-demand skill in the field of GIS, and I hope to make myself a more competitive applicant for jobs in the future with the skillset that I learn in this course. I also think it will be valuable simply for knowledge's sake to learn more about how computers and information systems function at a fundamental level.

## Assignment 2
I have chosen Python as the programming language that I will be learning in this course. Python is a very popular coding language, and it is one of the better languages to learn as a beginner because it emphasizes readability. As someone who has no prior programming experience, the relatively straightforward syntax of Python is appealing to me. Initially, I was using GDB Online to test my programs for Assignment 2, but then I downloaded Thonny, and I think that is the IDE I will be using for future assignments. Even after this course has ended, Python will be very useful to me moving forward with my GIS certificate because Python is commonly used in GIS applications (like ArcGIS Pro) to automate geoprocessing tasks.

## Assignment 3
This assignment was a good step up from the previous one. There was a lot of new material that I learned in this assignment, mainly, the different data types involved in programming and when it is best to use certain types over others. For example, when I was deciding which data type to use for miles/kilometers/meters/cm in my program, I initially thought I would just use an integer type. But as a long-distance runner, I know that many people count their mileage in half miles, or even in fractions smaller than that. No runner would say that a marathon is 26 miles, rather, they would say 26.2 miles. For this reason, I decided to go with the real (float) data type for my distance variables. I also learned that there could be several different ways to write code for the same outcome. The source code generated by my flowchart could have probably been written differently, perhaps more succinctly, and still resulted in the same (or functionally similar) output when the program is run. I intend to use the information I learned in this assignment in the future when working in ArcGIS Pro. Attribute tables for map layers in ArcGIS Pro store their data in integer, float, string, etc. It will be helpful for me to know which data types are most appropriate to use for which variables when filing or editing data in attribute tables in the future.

## Assignment 4
This session was similar to the last session, in terms of the material learned. But specific to this session, I learned that it is important to save program plans and source code from the past, because those plans and codes may be applicable to other projects in the future. I chose Activity 2 for this assignment, which was similar in its structure to Activity 3, despite having a different prompt and output. I was able to use my program plan and source code from Activity 3, which I created using Flowgorithm, to help me plan and write my program for Activity 2 without using Flowgorithm. I think keeping this in mind will be important going forward for me, as Python can be used to program workflows in ArcGIS for repetitive steps. Knowing that older code can be re-structured and applied to new workflows with similar inputs and outputs could be a great time-saver in the future.

## Assignment 5
In this assignment, I learned about the uses of functions in programming. Functions can be defined individually and specifically for whatever the developer needs, but there are also standard libraries that consist of reliably tested and generalized functions. I can only imagine how much time the standard library resource has saved for developers over the years. In this assignment, I didn’t have much trouble with my program plan, but creating my flowchart in Flowgorithm took much more time. Certain actions are required by Flowgorithm that I would probably not do when writing a program in an IDE- for example, I can’t name a function get_miles in Flowgorithm, rather, it must be GetMiles… but get_miles is acceptable (and easier to read/interpret) when writing out code in an IDE. I think this makes things a little more complicated than they need to be, but it was interesting to visually see how smaller functions can be defined separately and then tied together under the main function. Understanding functions will be useful for me in the future because all geoprocessing and workflow tools in ArcPy are provided as functions, so knowing how to utilize and program functions could save me a lot of time when working in ArcGIS Pro.

## Assignment 6
Assignment 6 provided an opportunity for more practice with the material from Chapter 3. After planning my program with Flowgorithm in Assignment 5, I felt confident that I could write my code for this assignment without making a flowchart. I used my program plan/source code from last week as a guide to help me, and that worked out fine. I did have to make some changes though as Activity 2 requires more variables and more computations than Activity 3 does. I am getting better at reading and understanding error messages in my IDE, it helps that Thonny provides clear error messages with references to the exact line where the error occurs. I will use the concepts that I learned in this session while working in ArcGIS pro for my other courses, and in my future career. ArcPy has a standard library of geoprocessing functions used to support workflows in ArcGIS, so it is beneficial for me to understand how those functions are written.

## Assignment 7
In this assignment, I learned about conditional statements in programming. I think selection and iteration control structures are interesting because they take more specifics/information into account than sequence control structures. Like in the case of the activity that I chose for this assignment (Activity 1), the answer to a question like “What is your hourly pay rate?” is not always straightforward, and a program that accounts for various circumstances will have more potential applications. But of course, this makes things more complicated, too. I struggled with writing my program plan, because it was difficult for me to determine where the if-then-else statement should be positioned in my program. Additionally, with any new information that I learn in programming, there are always new syntax requirements and reserved words to account for, and that is something I will only learn through practice. I have technically already used conditional statements when working in ArcGIS with simple geoprocessing tools. For example, if I am working with a dataset that contains more information that I need to use, I can clip that dataset using and/or statements to only include points that meet specific requirements that are useful to me.

## Assignment 8
In this assignment, I learned a lot about iteration structures in programming, specifically “for” loops. For loops are most useful when the number of iterations is known before running the loop; so, in the activity that I chose (Activity 1), a for loop would be a good choice because the user should know how many multiplication expressions they want to see. I had some trouble at first figuring out how to write my program plan based on the pseudocode in the textbook reading, mainly because for Activity 1, an increment input is not necessary, as the default increment (1) is what I would want to use for this program. Eventually, I was able to figure out the best way to structure things. I think for loops will be helpful for me working in GIS because sometimes when you are inputting/analyzing large amounts of data, you are often doing repetitive workflows. If I know how many repetitive actions I need to take when analyzing data, I can program a “for” loop and get things done much more efficiently.

## Assignment 9
In this assignment, I continued learning about iteration control structures with “while” loops. While loops are similar to for loops in some ways, mainly because both are test-before structures. But there are some differences to learn as well. For loops are most commonly used when the number of iterations is already known beforehand. While loops are more commonly used when the number of iterations is not known, but the stopping condition is known. All in all, I didn’t find it too difficult to transition from working with one to the other. I also think it is interesting to see how two different iteration control structures can be used for the same activity, and the same result can be achieved. Iterators such as while loops are used often in GIS work, as inputting and analyzing data can be very repetitive. There is a tool in ArcMap and ArcGIS Pro called “ModelBuilder” that can be used to create iterations for more efficient data processing. 

## Assignment 10
Assignment 10 focused on the do-while loop, which is the last loop that we are going to be working with in our iteration control structures series. Mentally I prefer to think of do-while loops as “repeat until” loops because that phrasing makes more sense to me. This assignment was tricky for me for a couple of reasons, the main reason being that Python does not have a reserved do-while loop function like many other programming languages do. Therefore, the do-while loop structure has to instead be emulated with a While True statement, a condition, and a break. This assignment was also difficult for me because do-while loops are test-after structures, so values that do not meet the condition are still passed through the loop before it terminates. For this reason, it took me some time to figure out how I would be able to terminate my loop for Activity 1 without incorporating the terminating value (in this case, any negative number) into the sum and average calculations. I think do-while loops could be practical for GIS analysis because sometimes you are doing repetitive actions with large amounts of data and you may not know how many repetitions you will be doing, but you do know you need to repeat certain actions at least once, and you know under what conditions you need those actions to occur. Although, since most programming in GIS is done in Python, it might often be easier to use a while or for structure instead of do-while.

## Assignment 11
Assignment 11 was an introduction to arrays. This assignment combined a lot of knowledge from past assignments, including loops and conditions. At first, I struggled quite a bit with my program plan for Activity 1. I wasn’t exactly clear on the program’s end goal, and I made things more complicated than they needed to be in my first draft. It was also a challenge not to have Flowgorithm to assist in writing source code. I have been practicing writing source code on my own without Flowgorithm, but I would often use the generated code from my flowchart to serve as a guide for syntax and structuring of my own code, so it was a bit of a challenge to be without that resource. Arrays are the ideal way to store values of the same type, and it is efficient to put information into an array and apply the same process to the whole array, rather than write out the same process for each element individually. I’m sure arrays are commonly used in any kind of data analytics field. There are times in GIS work when the same process needs to be applied to many objects, for example, creating a buffer zone around several different coordinate points. Creating an array of those points and then applying a buffer to the whole list would be the most efficient way to process that data.

## Assignment 12
This week, we continued learning about arrays, this time focusing on dynamic arrays instead of defined-value arrays. Dynamic arrays differ from defined-value arrays because they don’t have a fixed length, meaning, elements can be added or removed if necessary. This can be beneficial if a programmer wants to create a list without knowing the exact length of it beforehand. A common everyday example of a dynamic array is a contacts list on a cell phone. It is a sorted list where elements can be added or removed, and the length is not pre-determined. I found dynamic arrays were easier for me to understand than defined-value arrays. I think there are potentially more practical uses for a list that is flexible and can change in size. Dynamic arrays can be used in ArcPy, commonly consisting of coordinate pairs. Building a point feature class often requires that points be added or removed if their locations are inaccurate, so storing coordinate data in a dynamic array using the append function can be very practical.  

## Assignment 13
This assignment served as a deeper dive into the “string” data type. We have been using string throughout all assignments, but not really looking at string as an array. Because a string is technically an array of character elements, functions can be performed on a string. There were several new string functions that I was introduced to through Activity 2. I learned how to write a slice statement to print a string backward, and I also learned to use functions like “split” and “join” to remove duplicate spaces. Additionally, I learned how to use the “strip” function to remove leading and trailing whitespaces. There are a lot of different string functions that I look forward to exploring more in the future. String functions are commonly used in ArcMap and ArcGIS Pro. If I wanted to edit a string field in an attribute table, I could perform a string function on the entire field to efficiently get the result that I want. For example, if I was looking at a dataset with a field such as “city names”, and all the names started with a lowercase character, I could edit them to uppercase with the capitalize function. This would be much more efficient than going through each name and changing it manually.
