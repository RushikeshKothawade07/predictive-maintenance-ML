# Machine Predictive Maintenance Classification

### About Dataset<br><br>
## Machine Predictive Maintenance Classification Dataset<br>
Since real predictive maintenance datasets are generally difficult to obtain and in particular difficult to publish, we present and provide a synthetic dataset that reflects real predictive maintenance encountered in the industry to the best of our knowledge.<br><br>

The dataset consists of 10 000 data points stored as rows with 14 features in columns<br><br>

UID: unique identifier ranging from 1 to 10000 <br>
productID: consisting of a letter L, M, or H for low (50% of all products), medium (30%), and high (20%) as product quality variants and a variant-specific serial number<br>
air temperature [K]: generated using a random walk process later normalized to a standard deviation of 2 K around 300 K <br>
process temperature [K]: generated using a random walk process normalized to a standard deviation of 1 K, added to the air temperature plus 10 K. <br>
rotational speed [rpm]: calculated from powepower of 2860 W, overlaid with a normally distributed noise <br>
torque [Nm]: torque values are normally distributed around 40 Nm with an Ïƒ = 10 Nm and no negative values. <br>
tool wear [min]: The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process. and a 
'machine failure' label that indicates, whether the machine has failed in this particular data point for any of the following failure modes are true. <br>
Important : There are two Targets - Do not make the mistake of using one of them as feature, as it will lead to leakage. <br>
Target : Failure or Not <br>
Failure Type : Type of Failure
<br>
