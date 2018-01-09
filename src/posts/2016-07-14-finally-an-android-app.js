import React from 'react'

export const data = {
  tags: ['android', 'android app', 'personal project', 'java', 'app'],
  id: 'finally-an-android-app',
  date: { year: '2016', month: '07', day: '14' },
  desc: 'An android app that I had written which acts like a SMS receiving and recording sever and acts as an SMS gateway',
  title: 'Finally an android app',
  description: 'An android app that I had written which acts like a SMS receiving and recording sever and acts as an SMS gateway',
}
export default () => (
  <div>
    <h2>About the idea</h2>

    <p>After a couple of years after writing android apps, I chose to write an android app again. I had used Android Studio
                before but never tired serious android development after the very first time I tried it in Eclipse (the old times
                when there was not android studio).</p>

    <p>I chose a very old idea that I had before for voting. I thought I will make an app that accepts votes from people.
                This had to be something different from the regular apps. The main difference being that people should not have to
                install an app and/or should not have to open to a website to cast a vote. Hence, people should use the platform
                they are already using. Therefore I chose to go in for some messaging platform. The most popular platform out there
                is Whatsapp but again the problem with Whatsapp is that they don’t have any open APIs and moreover it’s illegal to
                reverse engineer the Whatsapp APIs. The other option is Telegram who have their APIs completely open. But the
                problem with doing it with Telegram is that they have very few users compared to Whatsapp. I had to settle
                somewhere in between the two choices. That’s the reason I chose traditional SMS over Telegram or Whatsapp.</p>

    <h2>Concept and design choices</h2>

    <p>Now it was time to design the app for voting but directly jumping for voting was a bit too much for processing and
                adding too much to the design and in addition to that some extra time in the development of the project. I thought
                of making it very simple and just storing the SMSes. So I finalised with the idea of writing an app that will
                accept registrations through the means of SMSes. Hence the name SMServer, a Short Message Server, the server with
                which people can accept SMSes from the user and store them.</p>

    <p>How the app worksː</p>

    <p>The basic idea is to accept the SMSes in a particular format . Suppose you are accepting the applications for a
                party that you are hosting it will be as follows. For example, let’s say I’m hosting an event and I want to accept
                the people’s names via SMS. So I will create a new form for accepting the people who are willing to join the event.
                Suppose the event is some music show, I will accept the applications in the following format.</p>

    <code>MUSIC&lt;space&gt;NAME&lt;space&gt;AGE</code>

    <p>Suppose John Doe is registering for an event, his message will be as follows:</p>

    <code>MUSIC John 27</code>

    <p>All the words that I’m accepting via the app are case insensitive. The reason being that there should be no mismatch
                between the words being just because of the case. At least the first word has to be kept case insensitive.</p>

    <h2>A screen to screen working for the app</h2>

    <h3>This is my emulator running Nexus 5</h3>
    <img alt="emulator" src="/res/images/smserver_images/01_emulator.png" />

    <h3>This is the starting screen when you first start the app</h3>
    <img alt="start_screen" src="/res/images/smserver_images/02_start_screen.png" />

    <h3>Now you click on the right-top corner menu button for creating a new form</h3>
    <img alt="main_menu" src="/res/images/smserver_images/03_main_menu.png" />

    <h3>These are the details that you have to fill up to accept registrations</h3>
    <img alt="new_form" src="/res/images/smserver_images/04_new_form.png" />

    <h3>Also included, date and time selectors</h3>
    <img alt="calender_selector" src="/res/images/smserver_images/05_calender_selector.png" />

    <h3>Fill up this form</h3>
    <img alt="filled_form" src="/res/images/smserver_images/07_filled_form.png" />

    <ul>
      <li>The name for the new form is the name that you want to give to the form which will accept registrations, the form name will be for your own reference</li>
      <li>The starting date and time are the date and time when the form should start accepting the entries</li>
      <li>Same goes for the ending time and date</li>
      <li>The first word is the first word that you have to enter to enter to accept the entry as an entry for this particular form</li>
      <li>The fields are the remaining words from the SMS that you will be accepting as fields in the form</li>
      <li>The form will be saved when you click the save button</li>
    </ul>


    <h3>On the main screen you will see the newly created form</h3>
    <img alt="main_screen_form_created" src="/res/images/smserver_images/10_main_screen_form_created.png" />

    <h3>You can either open the form</h3>
    <img alt="form_menu" src="/res/images/smserver_images/08_form_menu.png" />

    <h3>After opening the form you can see the details of the form</h3>
    <img alt="opened_form_no_entries" src="/res/images/smserver_images/09_opened_form_no_entries.png" />

    <h4>It will also list the phone numbers and date and time of the people who have just registered</h4>

    <h3>Now send an SMS to yourself with that format, I’ll send the same SMS (music john 28)</h3>
    <img alt="main_screen_form_created" src="/res/images/smserver_images/10_main_screen_form_created.png" />

    <h3>Then you can go to the main screen and come back by opening the form and you will see the entry for the newly received SMS</h3>
    <img alt="entry_made" src="/res/images/smserver_images/11_entry_made.png" />

    <h3>You can then click the form and say “Save the records” this will allow you to share the CSV file, keep in mind that you have to select an app that allows sending of CSV files, I’ll recommend to use an email app and you can also delete the form</h3>
    <img alt="form_menu" src="/res/images/smserver_images/08_form_menu.png" />

    <h3>You can see the server running in the background in the notification drawer</h3>
    <img alt="server_running_in_background" src="/res/images/smserver_images/12_server_running_in_background.png" />

    <h4>Now that you have seen how the app works, you can download the app by clicking
      <a href="https://drive.google.com/open?id=0B8ZGvtCVIoJgNlZPMnU3WHVXcFk">here</a>.
                Also, do test it on your own and report any bugs to me. You are also free to suggest any features to me if you want.</h4>
  </div>
)
