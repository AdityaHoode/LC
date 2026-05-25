from pathlib import Path
import re

# List of problems (without difficulty levels)
database_problems_list = [
    "175. Combine Two Tables",
    "176. Second Highest Salary",
    "177. Nth Highest Salary",
    "178. Rank Scores",
    "180. Consecutive Numbers",
    "181. Employees Earning More Than Their Managers",
    "182. Duplicate Emails",
    "183. Customers Who Never Order",
    "184. Department Highest Salary",
    "185. Department Top Three Salaries",
    "196. Delete Duplicate Emails",
    "197. Rising Temperature",
    "262. Trips and Users",
    "511. Game Play Analysis I",
    "550. Game Play Analysis IV",
    "570. Managers with at Least 5 Direct Reports",
    "577. Employee Bonus",
    "584. Find Customer Referee",
    "585. Investments in 2016",
    "586. Customer Placing the Largest Number of Orders",
    "595. Big Countries",
    "596. Classes With at Least 5 Students",
    "601. Human Traffic of Stadium",
    "602. Friend Requests II: Who Has the Most Friends",
    "607. Sales Person",
    "608. Tree Node",
    "610. Triangle Judgement",
    "619. Biggest Single Number",
    "620. Not Boring Movies",
    "626. Exchange Seats",
    "627. Swap Sex of Employees",
    "1045. Customers Who Bought All Products",
    "1050. Actors and Directors Who Cooperated At Least Three Times",
    "1068. Product Sales Analysis I",
    "1070. Product Sales Analysis III",
    "1075. Project Employees I",
    "1084. Sales Analysis III",
    "1141. User Activity for the Past 30 Days I",
    "1148. Article Views I",
    "1158. Market Analysis I",
    "1164. Product Price at a Given Date",
    "1174. Immediate Food Delivery II",
    "1179. Reformat Department Table",
    "1193. Monthly Transactions I",
    "1204. Last Person to Fit in the Bus",
    "1211. Queries Quality and Percentage",
    "1251. Average Selling Price",
    "1280. Students and Examinations",
    "1321. Restaurant Growth",
    "1327. List the Products Ordered in a Period",
    "1341. Movie Rating",
    "1378. Replace Employee ID With The Unique Identifier",
    "1393. Capital Gain/Loss",
    "1407. Top Travellers",
    "1484. Group Sold Products By The Date",
    "1517. Find Users With Valid E-Mails",
    "1527. Patients With a Condition",
    "1581. Customer Who Visited but Did Not Make Any Transactions",
    "1587. Bank Account Summary II",
    "1633. Percentage of Users Attended a Contest",
    "1661. Average Time of Process per Machine",
    "1667. Fix Names in a Table",
    "1683. Invalid Tweets",
    "1693. Daily Leads and Partners",
    "1729. Find Followers Count",
    "1731. The Number of Employees Which Report to Each Employee",
    "1741. Find Total Time Spent by Each Employee",
    "1757. Recyclable and Low Fat Products",
    "1789. Primary Department for Each Employee",
    "1795. Rearrange Products Table",
    "1873. Calculate Special Bonus",
    "1890. The Latest Login in 2020",
    "1907. Count Salary Categories",
    "1934. Confirmation Rate",
    "1965. Employees With Missing Information",
    "1978. Employees Whose Manager Left the Company",
    "2356. Number of Unique Subjects Taught by Each Teacher",
    "3220. Odd and Even Transactions",
    "3374. First Letter Capitalization II",
    "3421. Find Students Who Improved",
    "3436. Find Valid Emails",
    "3451. Find Invalid IP Addresses",
    "3465. Find Products with Valid Serial Numbers",
    "3475. DNA Pattern Recognition",
    "3482. Analyze Organization Hierarchy",
    "3497. Analyze Subscription Conversion",
    "3521. Find Product Recommendation Pairs",
    "3554. Find Category Recommendation Pairs",
    "3564. Seasonal Sales Analysis",
    "3570. Find Books with No Available Copies",
    "3580. Find Consistently Improving Employees",
    "3586. Find COVID Recovery Patients",
    "3601. Find Drivers with Improved Fuel Efficiency",
    "3611. Find Overbooked Employees",
    "3617. Find Students with Study Spiral Pattern",
    "3626. Find Stores with Inventory Imbalance",
    "3642. Find Books with Polarized Opinions",
    "3657. Find Loyal Customers",
    "3673. Find Zombie Sessions",
    "3705. Find Golden Hour Customers",
    "3716. Find Churn Risk Customers",
    "3764. Most Common Course Pairs",
    "3793. Find Users with High Token Usage",
    "3808. Find Emotionally Consistent Users",
    "3832. Find Users with Persistent Behavior Patterns"
]

pandas_problems_list = [
    "175. Combine Two Tables",
    "176. Second Highest Salary",
    "177. Nth Highest Salary",
    "178. Rank Scores",
    "180. Consecutive Numbers",
    "181. Employees Earning More Than Their Managers",
    "182. Duplicate Emails",
    "183. Customers Who Never Order",
    "184. Department Highest Salary",
    "185. Department Top Three Salaries",
    "196. Delete Duplicate Emails",
    "197. Rising Temperature",
    "262. Trips and Users",
    "511. Game Play Analysis I",
    "550. Game Play Analysis IV",
    "570. Managers with at Least 5 Direct Reports",
    "577. Employee Bonus",
    "584. Find Customer Referee",
    "585. Investments in 2016",
    "586. Customer Placing the Largest Number of Orders",
    "595. Big Countries",
    "596. Classes With at Least 5 Students",
    "601. Human Traffic of Stadium",
    "602. Friend Requests II: Who Has the Most Friends",
    "607. Sales Person",
    "608. Tree Node",
    "610. Triangle Judgement",
    "619. Biggest Single Number",
    "620. Not Boring Movies",
    "626. Exchange Seats",
    "627. Swap Sex of Employees",
    "1045. Customers Who Bought All Products",
    "1050. Actors and Directors Who Cooperated At Least Three Times",
    "1068. Product Sales Analysis I",
    "1070. Product Sales Analysis III",
    "1075. Project Employees I",
    "1084. Sales Analysis III",
    "1141. User Activity for the Past 30 Days I",
    "1148. Article Views I",
    "1158. Market Analysis I",
    "1164. Product Price at a Given Date",
    "1174. Immediate Food Delivery II",
    "1179. Reformat Department Table",
    "1193. Monthly Transactions I",
    "1204. Last Person to Fit in the Bus",
    "1211. Queries Quality and Percentage",
    "1251. Average Selling Price",
    "1280. Students and Examinations",
    "1321. Restaurant Growth",
    "1327. List the Products Ordered in a Period",
    "1341. Movie Rating",
    "1378. Replace Employee ID With The Unique Identifier",
    "1393. Capital Gain/Loss",
    "1407. Top Travellers",
    "1484. Group Sold Products By The Date",
    "1517. Find Users With Valid E-Mails",
    "1527. Patients With a Condition",
    "1581. Customer Who Visited but Did Not Make Any Transactions",
    "1587. Bank Account Summary II",
    "1633. Percentage of Users Attended a Contest",
    "1661. Average Time of Process per Machine",
    "1667. Fix Names in a Table",
    "1683. Invalid Tweets",
    "1693. Daily Leads and Partners",
    "1729. Find Followers Count",
    "1731. The Number of Employees Which Report to Each Employee",
    "1741. Find Total Time Spent by Each Employee",
    "1757. Recyclable and Low Fat Products",
    "1789. Primary Department for Each Employee",
    "1795. Rearrange Products Table",
    "1873. Calculate Special Bonus",
    "1890. The Latest Login in 2020",
    "1907. Count Salary Categories",
    "1934. Confirmation Rate",
    "1965. Employees With Missing Information",
    "1978. Employees Whose Manager Left the Company",
    "2356. Number of Unique Subjects Taught by Each Teacher",
    "2877. Create a DataFrame from List",
    "2878. Get the Size of a DataFrame",
    "2879. Display the First Three Rows",
    "2880. Select Data",
    "2881. Create a New Column",
    "2882. Drop Duplicate Rows",
    "2883. Drop Missing Data",
    "2884. Modify Columns",
    "2885. Rename Columns",
    "2886. Change Data Type",
    "2887. Fill Missing Data",
    "2888. Reshape Data: Concatenate",
    "2889. Reshape Data: Pivot",
    "2890. Reshape Data: Melt",
    "2891. Method Chaining",
    "3220. Odd and Even Transactions",
    "3374. First Letter Capitalization II",
    "3421. Find Students Who Improved",
    "3436. Find Valid Emails",
    "3451. Find Invalid IP Addresses",
    "3465. Find Products with Valid Serial Numbers",
    "3475. DNA Pattern Recognition",
    "3482. Analyze Organization Hierarchy",
    "3497. Analyze Subscription Conversion",
    "3521. Find Product Recommendation Pairs",
    "3554. Find Category Recommendation Pairs",
    "3564. Seasonal Sales Analysis",
    "3570. Find Books with No Available Copies",
    "3580. Find Consistently Improving Employees",
    "3586. Find COVID Recovery Patients",
    "3601. Find Drivers with Improved Fuel Efficiency",
    "3611. Find Overbooked Employees",
    "3617. Find Students with Study Spiral Pattern",
    "3626. Find Stores with Inventory Imbalance",
    "3642. Find Books with Polarized Opinions",
    "3657. Find Loyal Customers",
    "3673. Find Zombie Sessions",
    "3705. Find Golden Hour Customers",
    "3716. Find Churn Risk Customers",
    "3764. Most Common Course Pairs",
    "3793. Find Users with High Token Usage",
    "3808. Find Emotionally Consistent Users",
    "3832. Find Users with Persistent Behavior Patterns"
]

purely_pandas_problems_list = [
    "2877. Create a DataFrame from List",
    "2878. Get the Size of a DataFrame",
    "2879. Display the First Three Rows",
    "2880. Select Data",
    "2881. Create a New Column",
    "2882. Drop Duplicate Rows",
    "2883. Drop Missing Data",
    "2884. Modify Columns",
    "2885. Rename Columns",
    "2886. Change Data Type",
    "2887. Fill Missing Data",
    "2888. Reshape Data: Concatenate",
    "2889. Reshape Data: Pivot",
    "2890. Reshape Data: Melt",
    "2891. Method Chaining",
    "3617. Find Students with Study Spiral Pattern",
    "3626. Find Stores with Inventory Imbalance",
    "3642. Find Books with Polarized Opinions",
    "3657. Find Loyal Customers",
    "3673. Find Zombie Sessions",
    "3705. Find Golden Hour Customers",
    "3716. Find Churn Risk Customers",
    "3764. Most Common Course Pairs",
    "3793. Find Users with High Token Usage",
    "3808. Find Emotionally Consistent Users",
    "3832. Find Users with Persistent Behavior Patterns"
]

# Get actual files from folder
folder_path = Path(r"c:\Users\v-ahoode\Dev\LC\Database")
actual_files = {item.name for item in folder_path.iterdir() if item.is_file()}

# Extract problem numbers from list
list_numbers = {}
for problem in database_problems_list:
    num = int(problem.split('.')[0])
    list_numbers[num] = problem

# Extract problem numbers from files
file_numbers = {}
for file in actual_files:
    try:
        num = int(file.split('.')[0])
        file_numbers[num] = file
    except ValueError:
        # Skip files that don't start with a number
        pass

# Find missing problems (in list but not in files)
missing_numbers = set(list_numbers.keys()) - set(file_numbers.keys())

# Find extra problems (in files but not in list)
extra_numbers = set(file_numbers.keys()) - set(list_numbers.keys())

# Display results
print("=" * 80)
print("COMPARISON RESULTS")
print("=" * 80)

print(f"\nTotal problems in list: {len(list_numbers)}")
print(f"Total files in directory: {len(file_numbers)}")

if missing_numbers:
    print(f"\n❌ MISSING IN FOLDER ({len(missing_numbers)} problems):")
    for num in sorted(missing_numbers):
        print(f"   - {list_numbers[num]}")
else:
    print("\n✓ All problems from list are in the folder!")

if extra_numbers:
    print(f"\n⚠️  EXTRA IN FOLDER ({len(extra_numbers)} problems):")
    for num in sorted(extra_numbers):
        print(f"   - {file_numbers[num]}")
else:
    print("\n✓ No extra problems in folder!")

print("\n" + "=" * 80)