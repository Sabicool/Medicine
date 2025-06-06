---
date: 2025-04-06
---
# Patient Lists
1. Click ‘Patient List’ (top Toolbar): A List will pop up
2. Press the Spanner in top left: A pop-up will appear with two columns
3. Press ‘New’ button in bottom right
- From here two columns should appear; the left is the categories and the right is the subcategories
- Specific lists are outline below
## After Hours (Based on Location)
- Set up ward lists for each ward that you're covering
1. Double click 'Location' for 'Patient List Type'
2. Keep expanding the ‘Locations’ folder on the right column until specific enough
3. Choose the Hospital→Choose the Ward
4. Go to ‘Discharged Criteria’ (left column)→Various options appear on the right→Check ‘Only display patients that have not been Discharged’→Click ‘Finish’
5. Move that Ward List from ‘Available Lists’ to ‘Active Lists’ with the arrows
## Home Team (Based on Consultants)
1. Double click ‘Provider Group’ for the ‘Patient List Type’→Two columns appear
2. In the right column→Check all the Bosses your Team has
3. Now click ‘Locations’ (lef column)→‘Location List’ appears on the right→ Check your Hospital (right column). Remember that this is for inpatients only; avoid clicking ‘Clinics’ unless you see them there
4. You may also need to go to ‘Encounter type’ (lef column) and check ‘Inpatients’ only
5. Go to ‘Discharged Criteria’ (lef column)→Various options appear on the right →Check ‘Only display patients that have not been Discharged’
6. Name your List at ‘Enter a name for the List:’
7. Click ‘Next’ if you wish to proxy people (see section ‘List maintenance’)
8. Done: You now have an auto-populating List of patients who are all under your Bosses. Your List will now self-update at will and patients will of themselves appear and disappear from it as soon as they are Admitted or Discharged
- You can also choose ‘Medical Service’ (lef column) for Medical Terms with only one Team, e.g. choose ‘Endocrinology’ as the ‘Service’ and follow the above scheme instead of ‘Provider Group’ or any other method as you require
	- But you cannot add or remove any patients from it, hence patients your team has TOC'ed are annoying as you need to wait for the ward clerk to update the system and discharged patients are annoying as they vanish (unless you change the discharge criteria to discharged in the last xxx days to find them again)
	- Additionally consults can't be added either
## Custom List
- You get the ability to add or delete patients from the list at will but it won't do anything automatically
1. Double click 'Custom for the 'Patient List Type'
2. Enter a Name and hit 'Finish' -> Done
- Can use it as a team list by copying all patients from the auto-populating one (medical service one above) and then adding patients to it for whatever purpose (e.g. consults, after hours, follow-up) and remove them if you no longer need them
- You can also right click on patients in the custom list and click 'Add to a Patient List' or 'Remove Patient from List'
## Consultant List
- Create this list when the registrar says "[consultant name] is rounding today"
- First sort the List based on Location, then Consultant (click each column heading); then simply highlight, right click and select ‘Hide’ for all patients not under the Rounding Consultant

## Rounds List
- Regular list with columns that can display certain results/investigations/patient numbers; particularly useful on surgical terms where you often do not know all the patients because of high turnover
- Consider setting it up to show things like: temperature, HR, sats, Hb, WBC, Br, eGFR, Cr
	- However note that it does not show the trend or changes
	- Cannot do subtotals so can be limited use for drain outputs but can use the daily output
- For printing just screenshot and print it in word
- Set up
	- Click rounds list (next to multi-patient task list) -> choose the list you want a rounds list of -> a window will appear -> check select all and dropdown then select assigned -> rounds list will appear and auto-populate
	- Note that all the columns are moveable and shrinkable so do it just like in excell for pinting space issues
	- To get parameters:
		1. Find the far-right column and expand its size as in excel
		2. Go to the top of the column and right click -> select 'insert column' (or delete column)
		3. Start expanding folders and choose the results you want
		4. Click ALLOCFSETS → Then ALLRESLTSECT → Then ALLSERVSECTS → Then you reach a few choices
			- Laboratory: self-explanatory
			- Patient care: nursing obs
		5. Once desired parameter is highlighted -> click next and choose how far back in time you want to look for that result
		6. Click next again and enter a header or name for the column (short as possible) then finish
		7. Screen print and print from Word via landscape
## Personalised List
- You don't have space in the above lists to note down in the lists above
- Copy and paste the list to excel (always into column A)
- One time formatting of adjusting width
	- Add two other empty columns: one for results to note and the other for jobs
	- Consider deleting the admit reason if you have time to write up some actual diagnoses and past history of the patient
- Landscape and double sided printing
	- See if it fits by going to the print tab and then back to the usual cells
	- Dotted lines should now appear denoting the printable space
	- Shrink your list to that space using wrap text, cutting attending consultant shrinking the font
	- In newer excel may need to be through file -> page setup -> landscape (consider reducing margins and adding header) and view -> page break preview/page layout
- **Save** this perfectly formatted list for the rest of the days on the term
- Even if the patients change you can copy and paste on top of this and delete the columns you don't want (can even record a macro for this)
- Have the columns in the following order
	- Location
	- Patient record number
	- Patient name
	- Age
	- Attending consult
	- Admit reason/clinical history
	- Other columns as you please

# List Maintenance
- You will often need to add new consultants, change the order of columns etc. There are 3 main ways to maintain/customise your list:
	1. List maintenance (spanner icon): Chooses lists. Pop up two columns 'Available Lists' and 'Active Lists'
		- Left/right arrow makes the selected list active or inactive
			- Active lists appear as a tab on the patient list screen
			- Available lists are ones you don't need for now (e.g. list of prior terms)
		- Up/down arrow shuffles the physical order of your active lists
		- You can also use this to make new lists
	2. List properties (pointing finger icon): Changes lists structurally
		- Adjusts the properties of the list you're now in
			- Will bring you back to the page where you first set up the list to modify if needed (e.g. changing 'discharge' criteria to find a discharged patient with no discharge papers)
			- Not used unless doing something like adding a new boss
		- Proxying which allows other people use your list
			- Click proxy tab on the top → click new → find the reg under provider (last name first) -> access is mostly full -> grant access for a reasonable time -> click apply and ok -> tell the reg to transfer it from their available list to their active list
	3. Customise columns (red/yellow pen on paper icon)
		- Move active and available columns with the arrows then shuffle them up or down using the blue arrow
		- Click and simply add categories that you want and delete what you don’t. While on the left, you can organise column order by up and down arrows and at last save
		- Useful columns to include
			- Room and bed
			- Patient record number
			- Name
			- Age
			- Admit reason
			- Attending physician
			- New results
- Other functions
	- Right click on patient row to bring up additional options like sort or hide (which is useful to count number of patients using the number of patients hidden)
# Task Lists
## Handover/Multi-Patient Task List
- List of all patients in the hospital who need something overnight/during the weekend (e.g. monitoring, repeat reviews/investigations/management)
- Going home and giving people work to do:
	1. Copy the history and relevant information into word before opening the list as you are not able to access this information while creating the consult form
	2. Go to Ad hoc -> look down the long list until you see Medical Handover -> Select Medical Handover Summary Form and Chart
	3. Brings up a lot of stuff, fill out areas on Situation (actual problem) and recommendation (what needs to be done); fill out other parts relevant to handover
	4. Check the other yellow boxes as appropriate
	5. Call the after hours person and personally hand over if its important
	- Also give information on what do once the results come back (i.e. do this if positive, do this if negative)
- Finding work to do as overnight/relief person (also see below [[#Task Manager JMO Jobs List]])
	1. Go to multi-parent task list -> click handover tasks/handover tab and peruse jobs -> click yellow/tab square next to each patient job to signify completion
	2. To modify your multi-patient task list right click department view (top bar in grey) -> select customise patient view -> pick your location by either hospital or ward -> go to side tab 'Times Frames' -> select generic time frame -> then put in the range of times you want to see jobs for
	3. Remember to click save under location filters to save repeating this process each time
	4. Log in and log out and refresh if it doesn't auto-update
	5. Click the jobs to see what needs doing
	6. Start triaging then doing jobs
	7. If the handover form doesn't appear -> go to patient profile and pretend you're charting a handover -> handover form should appear filled with the instructions
## Task Manager: JMO Jobs List
- Set up one List type for each type of After Hours shift there is:
	- Go to task manager (same column as patient list) -> on the left column -> click + sign (new list) -> choose facility/hospital -> choose wards you cover -> click refresh sign (generate list) -> populates the jobs in your area of cover -> click save sign -> name it -> saved for future reference
	- You can simply click on whichever shift type you're working an the job lists will populate automatically
- Can mark complete and cancel on the various tasks
- The list can also be filtered by clicking the column headings
	- Can batch tasks by grouping by task (e.g. recharting all med charts together)
	- Patient information: location
# Other Lists
## Emergency Department List When Not Physically There
- You can see all ED patients in PowerChart
- Go to patient dashboard -> click emergency medicine -> choose your institution -> click emergency dept.-All patients -> see list of all ed patients
## Journey Board: Allied Health Progress List
- Journey board (same bar as patient list) -> select a ward and choose the ward