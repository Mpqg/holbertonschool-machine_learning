 ![Project badge](https://intranet.hbtn.io/assets/pathway/002_color-261c5d8dcd9df7930ced5c51da7ac8a20266ad8b3861fea9ce55fbc3a4df3fd7.png) 
# Plotting
## Details
Novice By: Alexa Orrico, Software Engineer at Holberton School Weight: 1 ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/b4601426ad02130836f9.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230803%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230803T022322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=46214253450483c7e53192e6b260cb35dfed98695d30386aeba7623d61f1c42f) 

## Resources
Read or watch :
* [Plot (graphics)](https://intranet.hbtn.io/rltoken/swUAw_dV4-PhFth6wSzU1w) 

* [Scatter plot](https://intranet.hbtn.io/rltoken/ukujmh-I_E6VTCLeJLiANw) 

* [Line chart](https://intranet.hbtn.io/rltoken/gO3-Klt1z0tJeVU1aJD9qg) 

* [Bar chart](https://intranet.hbtn.io/rltoken/JLN6oUJ6zbzZPW2i4Z_TaQ) 

* [Histogram](https://intranet.hbtn.io/rltoken/FXDyUjw0H15E7AmmTo35LA) 

* [Pyplot tutorial](https://intranet.hbtn.io/rltoken/Lq1HDu2VEMZi-yE_7ltscw) 

* [matplotlib.pyplot](https://intranet.hbtn.io/rltoken/dLvKK7IoDp4iJ1SDOfXjbA) 

* [matplotlib.pyplot.plot](https://intranet.hbtn.io/rltoken/xnkRJa0RUk11gHCn_4d7wg) 

* [matplotlib.pyplot.scatter](https://intranet.hbtn.io/rltoken/G31zxaALPB8X6Tl0pGBKZg) 

* [matplotlib.pyplot.bar](https://intranet.hbtn.io/rltoken/vWYnFhqY9BR2GcjwZeL93Q) 

* [matplotlib.pyplot.hist](https://intranet.hbtn.io/rltoken/eK68OpXged-N3ln1JKx6uw) 

* [matplotlib.pyplot.xlabel](https://intranet.hbtn.io/rltoken/thmt08lRjDru1ZveGf5K_A) 

* [matplotlib.pyplot.ylabel](https://intranet.hbtn.io/rltoken/OVXA56hPedxzZQUsTsb3NQ) 

* [matplotlib.pyplot.title](https://intranet.hbtn.io/rltoken/69jaiU_qxZXdmtw2H74V0w) 

* [matplotlib.pyplot.subplot](https://intranet.hbtn.io/rltoken/tJyJnYmU379spf1PwDS5NA) 

* [matplotlib.pyplot.subplots](https://intranet.hbtn.io/rltoken/hKc-OtsJ9jlFXFnpdw4rEA) 

* [matplotlib.pyplot.subplot2grid](https://intranet.hbtn.io/rltoken/XlkmUFK2Q5etIUNXAfLl-A) 

* [matplotlib.pyplot.suptitle](https://intranet.hbtn.io/rltoken/t45q5xSfiqFDoCsFTaQuhQ) 

* [matplotlib.pyplot.xscale](https://intranet.hbtn.io/rltoken/DOhIVi9vhIx5PwVwX1YYLw) 

* [matplotlib.pyplot.yscale](https://intranet.hbtn.io/rltoken/yPvF0-aSA20E-Ooa-Yi5XQ) 

* [matplotlib.pyplot.xlim](https://intranet.hbtn.io/rltoken/ElRUPhxnBRJ04JjWyO1mJg) 

* [matplotlib.pyplot.ylim](https://intranet.hbtn.io/rltoken/NqDCA5ih935PeOwUsdx3rw) 

* [mplot3d tutorial](https://intranet.hbtn.io/rltoken/AYQjFMZVls_eLrJl7ELDbA) 

* [additional tutorials](https://intranet.hbtn.io/rltoken/CUnX6P9AajVauF-4iDQORw) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/T6RpmzN1RWzgtgh20Mki8Q) 
 ,  without the help of Google :
### General
* What is a plot?
* What is a scatter plot? line graph? bar graph? histogram?
* What is  ` matplotlib ` ?
* How to plot data with  ` matplotlib ` 
* How to label a plot
* How to scale an axis
* How to plot multiple sets of data at the same time
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 16.04 LTS using  ` python3 `  (version 3.5)
* Your files will be executed with  ` numpy `  (version 1.15) and  ` matplotlib `  (version 3.0)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/env python3 ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the  ` pycodestyle `  style (version 2.5)
* All your modules should have documentation ( ` python3 -c 'print(__import__("my_module").__doc__)' ` )
* All your classes should have documentation ( ` python3 -c 'print(__import__("my_module").MyClass.__doc__)' ` )
* All your functions (inside and outside a class) should have documentation ( ` python3 -c 'print(__import__("my_module").my_function.__doc__)' `  and  ` python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ` )
* Unless otherwise noted, you are not allowed to import any module
* All your files must be executable
* The length of your files will be tested using  ` wc ` 
## More Info
### Installing Matplotlib 3.0
 ` pip install --user matplotlib==3.0
pip install --user Pillow
sudo apt-get install python3-tk
 ` To check that it has been successfully downloaded, use   ` pip list `  .
### Configure X11 Forwarding
Update your   ` Vagrantfile `   to include the following:
 ` Vagrant.configure(2) do |config|
  ...
  config.ssh.forward_x11 = true
end
 ` If you are running   ` vagrant `   on a Mac, you will have to install  [XQuartz](https://intranet.hbtn.io/rltoken/NIwcotPcUfkjTAHYdmEHBg) 
  and restart your computer.
If you are running   ` vagrant `   on a Windows computer, you may have to follow  [these instructions](https://intranet.hbtn.io/rltoken/oa02zPG7ZuYMtuu40ilvog) 
 .
Once complete, you should simply be able to   ` vagrant ssh `   to log into your VM and then any GUI application should forward to your local machine.
Hint for  ` emacs `  users: you will have to use  ` emacs -nw `  to prevent it from launching its GUI.
## Tasks
### 0. Line Graph
          mandatory         Progress vs Score  Task Body Complete the following source code to plot   ` y `   as a line graph:
*  ` y `  should be plotted as a solid red line
* The x-axis should range from 0 to 10
```bash
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# your code here

```
 ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/664b2543b48ef4918687.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230803%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230803T022322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9baef33031cb9e23796515345041ae6fac3538425382e83a8c8fdbea6bd3240c) 

 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-machine_learning ` 
* Directory:  ` math/plotting ` 
* File:  ` 0-line.py ` 
Checker Docker image:
 Self-paced manual review Please review your task manually with the following checklist[](https://intranet.hbtn.io/projects/2280#task-21071-carousel) 
Code passes   ` pycodestyle ` 
The line on the graph is red
The x-axis goes exactly from 0 to 10
Plot displays a cubic line graph
[](https://intranet.hbtn.io/projects/2280#task-21071-carousel) 
 Panel footer - Controls 
### 1. Scatter
          mandatory         Progress vs Score  Task Body Complete the following source code to plot   ` x ↦ y `   as a scatter plot:
* The x-axis should be labeled  ` Height (in) ` 
* The y-axis should be labeled  ` Weight (lbs) ` 
* The title should be  ` Men's Height vs Weight ` 
* The data should be plotted as magenta points
```bash
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

# your code here

```
 ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/1b143961d254e65afa2c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230803%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230803T022322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=df9cd9cfba8c87bc0a16ad572be37b344ccf133219b68eab53d5c3052adc9fce) 

 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-machine_learning ` 
* Directory:  ` math/plotting ` 
* File:  ` 1-scatter.py ` 
Checker Docker image:
 Self-paced manual review Please review your task manually with the following checklist[](https://intranet.hbtn.io/projects/2280#task-21072-carousel) 
Code passes   ` pycodestyle ` 
The title is “Men’s Height vs Weight”
The x-axis is labeled “Height (in)”
The y-axis is labeled “Weight (lbs)”
The data points are magenta
The data is presented as a scatter plot and looks exactly like the example
[](https://intranet.hbtn.io/projects/2280#task-21072-carousel) 
 Panel footer - Controls 
### 2. Change of scale
          mandatory         Progress vs Score  Task Body Complete the following source code to plot   ` x ↦ y `   as a line graph:
* The x-axis should be labeled  ` Time (years) ` 
* The y-axis should be labeled  ` Fraction Remaining ` 
* The title should be  ` Exponential Decay of C-14 ` 
* The y-axis should be logarithmically scaled
* The x-axis should range from 0 to 28650
```bash
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# your code here

```
 ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/2b6334feb069ae1b6014.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230803%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230803T022322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cd09015dc3aca86a0680998a631636866bbab2a1bd7d86f36832bbfd64d46324) 

 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-machine_learning ` 
* Directory:  ` math/plotting ` 
* File:  ` 2-change_scale.py ` 
Checker Docker image:
 Self-paced manual review Please review your task manually with the following checklist[](https://intranet.hbtn.io/projects/2280#task-21073-carousel) 
Code passes   ` pycodestyle ` 
The x-axis is labeled “Time (years)”
The y-axis is labeled “Fraction Remaining”
The title is “Exponential Decay of C-14”
The y-axis is logarithmically scaled
The x-axis ranges exactly from 0 to 28650
The plot displays a line graph exactly like the example
[](https://intranet.hbtn.io/projects/2280#task-21073-carousel) 
 Panel footer - Controls 
### 3. Two is better than one
          mandatory         Progress vs Score  Task Body Complete the following source code to plot   ` x ↦ y1 `   and   ` x ↦ y2 `   as line graphs:
* The x-axis should be labeled  ` Time (years) ` 
* The y-axis should be labeled  ` Fraction Remaining ` 
* The title should be  ` Exponential Decay of Radioactive Elements ` 
* The x-axis should range from 0 to 20,000
* The y-axis should range from 0 to 1
*  ` x ↦ y1 `  should be plotted with a dashed red line
*  ` x ↦ y2 `  should be plotted with a solid green line
* A legend labeling  ` x ↦ y1 `  as  ` C-14 `  and  ` x ↦ y2 `  as  ` Ra-226 `  should be placed in the upper right hand corner of the plot
```bash
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# your code here

```
 ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/39eac4e8c8eb71469784.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230803%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230803T022322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f462bf56e306e3461f8ca47fceb72dd7bb7b388775eae34a2778e86c6225b4a4) 

 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-machine_learning ` 
* Directory:  ` math/plotting ` 
* File:  ` 3-two.py ` 
Checker Docker image:
 Self-paced manual review Please review your task manually with the following checklist[](https://intranet.hbtn.io/projects/2280#task-21074-carousel) 
Code passes   ` pycodestyle ` 
The x-axis is labeled “Time (years)”
The y-axis is labeled “Fraction Remaining”
The title is “Exponential Decay of Radioactive Elements”
The x-axis ranges exactly from 0 to 20,000
The y-axis ranges exactly from 0 to 1
Two lines are plotted exactly like in the example
The top line is red and dotted
The bottom line is green and solid
A legend exists in the upper right hand corner and shows a dotted red line as “C-14” and a solid green line as “Ra-266”
[](https://intranet.hbtn.io/projects/2280#task-21074-carousel) 
 Panel footer - Controls 
### 4. Frequency
          mandatory         Progress vs Score  Task Body Complete the following source code to plot a histogram of student scores for a project:
* The x-axis should be labeled  ` Grades ` 
* The y-axis should be labeled  ` Number of Students ` 
* The x-axis should have bins every 10 units
* The title should be  ` Project A ` 
* The bars should be outlined in black
```bash
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here

```
 ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/10a48ad296d16ee8fb63.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230803%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230803T022322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9712c4f836f0c5cdf567275ea1860da7eca6856beda976df6580996497664a42) 

 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-machine_learning ` 
* Directory:  ` math/plotting ` 
* File:  ` 4-frequency.py ` 
Checker Docker image:
 Self-paced manual review Please review your task manually with the following checklist[](https://intranet.hbtn.io/projects/2280#task-21075-carousel) 
Code passes   ` pycodestyle ` 
The x-axis is labeled “Grades”
The y-axis is labeled “Number of Students”
The title is “Project A”
The plot displays a bar graph that looks exactly like the example
The x-axis has a bin every 10 units
The bars are outlined in black
[](https://intranet.hbtn.io/projects/2280#task-21075-carousel) 
 Panel footer - Controls 
### 5. All in One
          mandatory         Progress vs Score  Task Body Complete the following source code to plot all 5 previous graphs in one figure:
* All axis labels and plot titles should have a font size of  ` x-small `  (to fit nicely in one figure)
* The plots should make a 3 x 2 grid
* The last plot should take up two column widths (see below)
* The title of the figure should be  ` All in One ` 
```bash
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here

```
 ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/e58d423ffd060a779753.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230803%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230803T022322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=de8a0ff00f953e7445437a93406f29abfe5320f89cc0a6141855bbf92707fa3e) 

 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-machine_learning ` 
* Directory:  ` math/plotting ` 
* File:  ` 5-all_in_one.py ` 
Checker Docker image:
 Self-paced manual review Please review your task manually with the following checklist[](https://intranet.hbtn.io/projects/2280#task-21077-carousel) 
Code passes   ` pycodestyle ` 
All axis labels and plot titles have a font size of   ` x-small ` 
The plots make a 3 x 2 grid
The last plot takes up two column widths
The title of the figure is be “All in One”
The figure looks exactly like the example
[](https://intranet.hbtn.io/projects/2280#task-21077-carousel) 
 Panel footer - Controls 
### 6. Stacking Bars
          mandatory         Progress vs Score  Task Body Complete the following source code to plot a stacked bar graph:
*  ` fruit `  is a matrix representing the number of fruit various people possess* The columns of  ` fruit `  represent the number of fruit  ` Farrah ` ,  ` Fred ` , and  ` Felicia `  have, respectively
* The rows of  ` fruit `  represent the number of  ` apples ` ,  ` bananas ` ,  ` oranges ` , and  ` peaches ` , respectively

* The bars should represent the number of fruit each person possesses:* The bars should be grouped by person, i.e, the horizontal axis should have one labeled tick per person
* Each fruit should be represented by a specific color:*  ` apples `  = red
*  ` bananas `  = yellow
*  ` oranges `  = orange ( ` #ff8000 ` )
*  ` peaches `  = peach ( ` #ffe5b4 ` )
* A legend should be used to indicate which fruit is represented by each color

* The bars should be stacked in the same order as the rows of  ` fruit ` , from bottom to top
* The bars should have a width of  ` 0.5 ` 

* The y-axis should be labeled  ` Quantity of Fruit ` 
* The y-axis should range from 0 to 80 with ticks every 10 units
* The title should be  ` Number of Fruit per Person ` 
```bash
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# your code here

```
 ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/10/8058e8f96e697612d50d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230803%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230803T022322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=17d02d482ee02daf4b8f2f6233c860c0deda5e394bae977634a0cb93fc4a2d64) 

 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-machine_learning ` 
* Directory:  ` math/plotting ` 
* File:  ` 6-bars.py ` 
Checker Docker image:
 Self-paced manual review Please review your task manually with the following checklist[](https://intranet.hbtn.io/projects/2280#task-21078-carousel) 
Code passes   ` pycodestyle ` 
The y-axis is labeled “Quantity of Fruit”
The y-axis ranges exactly from 0 to 80 with ticks every 10 units
The title is “Number of Fruit per Person”
The horizontal axis has one labeled tick per person (  ` Farrah `  ,   ` Fred `  , and   ` Felicia `  , respectively)
The bars are stacked as   ` apples `  ,   ` bananas `  ,   ` oranges `  , and   ` peaches `  , respectively, from bottom to top
A legend exists with   ` apples `   = red,   ` bananas `   = yellow,   ` oranges `   = orange (#ff8000), and   ` peaches `   = peach (#ffe5b4)
The bars have a width of 0.5
The plot looks exactly like the example
[](https://intranet.hbtn.io/projects/2280#task-21078-carousel) 
 Panel footer - Controls 
[Done with the mandatory tasks? Unlock 2 advanced tasks now!](https://intranet.hbtn.io/projects/2280/unlock_optionals) 

### Score
 ![Project badge](https://intranet.hbtn.io/assets/pathway/002_color-261c5d8dcd9df7930ced5c51da7ac8a20266ad8b3861fea9ce55fbc3a4df3fd7.png) 

Please review all the  manual checks before you launch the project review.
Skip this project[Previous project](https://intranet.hbtn.io/projects/2275) 
