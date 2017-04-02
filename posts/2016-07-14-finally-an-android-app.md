---
layout: post
title: Finally an android app
categories: [projects]
tags: [android, android app, personal project, java, app]
fullview: false
comments: true
---

About the idea
--------------
After a couple of years after writing android apps, I chose to write an android app again. I had used Android Studio before but never tired serious android development after the very first time I tried it in Eclipse (the old times when there was not android studio).

<!--more-->

I chose a very old idea that I had before for voting. I thought I will make an app that accepts votes from people. This had to be something different from the regular apps. The main difference being that people should not have to install an app and/or should not have to open to a website to cast a vote. Hence, people should use the platform they are already using. Therefore I chose to go in for some messaging platform. The most popular platform out there is Whatsapp but again the problem with Whatsapp is that they don’t have any open APIs and moreover it’s illegal to reverse engineer the Whatsapp APIs. The other option is Telegram who have their APIs completely open. But the problem with doing it with Telegram is that they have very few users compared to Whatsapp. I had to settle somewhere in between the two choices. That’s the reason I chose traditional SMS over Telegram or Whatsapp.

Concept and design choices
--------------------------
Now it was time to design the app for voting but directly jumping for voting was a bit too much for processing and adding too much to the design and in addition to that some extra time in the development of the project. I thought of making it very simple and just storing the SMSes. So I finalised with the idea of writing an app that will accept registrations through the means of SMSes. Hence the name SMServer, a Short Message Server, the server with which people can accept SMSes from the user and store them.

How the app worksː
------------------
The basic idea is to accept the SMSes in a particular format . Suppose you are accepting the applications for a party that you are hosting it will be as follows. For example, let’s say I’m hosting an event and I want to accept the people’s names via SMS. So I will create a new form for accepting the people who are willing to join the event. Suppose the event is some music show, I will accept the applications in the following format.

```
MUSIC<space>NAME<space>AGE
```

Suppose John Doe is registering for an event, his message will be as follows:

```
MUSIC John 27
```

All the words that I’m accepting via the app are case insensitive. The reason being that there should be no mismatch between the words being just because of the case. At least the first word has to be kept case insensitive.

A screen to screen working for the app
--------------------------------------

### This is my emulator running Nexus 5
![emulator]({{ site.BASE_PATH }}/images/media/smserver_images/01_emulator.png){:width="256px"}

### This is the starting screen when you first start the app
![start_screen]({{ site.BASE_PATH }}/images/media/smserver_images/02_start_screen.png){:width="256px"}

### Now you click on the right-top corner menu button for creating a new form
![main_menu]({{ site.BASE_PATH }}/images/media/smserver_images/03_main_menu.png){:width="256px"}

### These are the details that you have to fill up to accept registrations
![new_form]({{ site.BASE_PATH }}/images/media/smserver_images/04_new_form.png){:width="256px"}

### Also included, date and time selectors
![calender_selector]({{ site.BASE_PATH }}/images/media/smserver_images/05_calender_selector.png){:width="256px"} ![emulator]({{ site.BASE_PATH }}/images/media/smserver_images/06_time_selector.png){:width="256px"}

### Fill up this form
![filled_form]({{ site.BASE_PATH }}/images/media/smserver_images/07_filled_form.png){:width="256px"}

- The name for the new form is the name that you want to give to the form which will accept registrations, the form name will be for your own reference
- The starting date and time are the date and time when the form should start accepting the entries
- Same goes for the ending time and date
- The first word is the first word that you have to enter to enter to accept the entry as an entry for this particular form
- The fields are the remaining words from the SMS that you will be accepting as fields in the form
- The form will be saved when you click the save button


### On the main screen you will see the newly created form
![main_screen_form_created]({{ site.BASE_PATH }}/images/media/smserver_images/10_main_screen_form_created.png){:width="256px"}

### You can either open the form
![form_menu]({{ site.BASE_PATH }}/images/media/smserver_images/08_form_menu.png){:width="256px"}

### After opening the form you can see the details of the form
![opened_form_no_entries]({{ site.BASE_PATH }}/images/media/smserver_images/09_opened_form_no_entries.png){:width="256px"}

##### It will also list the phone numbers and date and time of the people who have just registered


### Now send an SMS to yourself with that format, I’ll send the same SMS (music john 28)
![main_screen_form_created]({{ site.BASE_PATH }}/images/media/smserver_images/10_main_screen_form_created.png){:width="256px"}

### Then you can go to the main screen and come back by opening the form and you will see the entry for the newly received SMS
![entry_made]({{ site.BASE_PATH }}/images/media/smserver_images/11_entry_made.png){:width="256px"}

### You can then click the form and say “Save the records” this will allow you to share the CSV file, keep in mind that you have to select an app that allows sending of CSV files, I’ll recommend to use an email app and you can also delete the form
![form_menu]({{ site.BASE_PATH }}/images/media/smserver_images/08_form_menu.png){:width="256px"}

### You can see the server running in the background in the notification drawer
![server_running_in_background]({{ site.BASE_PATH }}/images/media/smserver_images/12_server_running_in_background.png){:width="256px"}

##### Now that you have seen how the app works, you can download the app by clicking [here](https://drive.google.com/open?id=0B8ZGvtCVIoJgNlZPMnU3WHVXcFk). Also, do test it on your own and report any bugs to me. You are also free to suggest any features to me if you want.
