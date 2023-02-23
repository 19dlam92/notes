**FUNCTIONS**

def hello ( **parameter = " optional argument "** ):
> print( " Hello " + parameter)
> 
> hello ( " Beau " )
> hello ( " Quincy " )
> hello ( )
> 
> displays
> ---> Hello Beau
> ---> Hello Quincy
> ---> **IF** name wasn't specified it **DEFAULTS** to **" optional argument "**
>         ---> " optional argument " can be named anything
> 
def hello ( **parameter1, parameter2** ):
> print( " Hello " + parameter1 + ", you can be combined with " + parameter2)
> 
> displays
> --->


**PARAMETER VS ARGUMENTS**

Parameters - values accepted by the function inside the function definition

Arguments - values we pass to the function when we call it
> 
> can have a default value