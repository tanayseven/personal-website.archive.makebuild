import React from 'react'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import Card from 'material-ui/es/Card/Card'
import theme from '../components/theme'

export default () => (
  <MuiThemeProvider theme={theme}>
    <Card>
      <div>
        <div>
          <h2>Skills (Non technology specific)</h2>
          <div>Test Driven Software Development (6.5)</div>
          <div>Web based software development (6) </div>
          <div>Follow scrum in software development (5)</div>
          <div>Learning a new language/technology stars(6)</div>
          <div>Structured Programming (7)</div>
          <div>Object Oriented Programming (6)</div>
          <div>Functional Programming stars(5)</div>
        </div>
        <div>
          <h2>Skills (Language/Technology)</h2>
          <div>Python (7)</div>
          <div>Flask - Python (6)</div>
          <div>Django - Python (3)</div>
          <div>Docker (3)</div>
          <div>Java (5)</div>
          <div>Native Android (5)</div>
          <div>JavaScript (5)</div>
          <div>Clojure (4)</div>
          <div>HTML/CSS (6)</div>
          <div>SQL (5)</div>
        </div>
        <div>
          <h2>Work Experience</h2>
          <div>
            <h3>Internship at Tata Consultancy Services</h3>
            <p>December 2013 to January 2014</p>
            <ul>
              <li>Worked on profiling an embedded application written for Windows Embedded Standard 7</li>
              <li>Technology used to develop was C# and profilers used were Red Gate ANTS and CLR</li>
            </ul>
          </div>
          <div>
            <h3>Software Craftsman at Nelkinda Software Craft</h3>
            <p>September 2016 to 2017</p>
            <ul>
              <li>Working on project that include Flask - Python and Native Android - Java development</li>
              <li>Daily use of practices like scrum and TDD in the software development process</li>
            </ul>
          </div>
        </div>
        <div>
          <h2>Personal Projects</h2>
          <div>
            <h3>Pitchy Bird</h3>
            <p>A browser based Flappy Bird inspired game controlled by using voice</p>
          </div>
          <div>
            <h3>JTankWars</h3>
            <p>Made as a part of my final project for Diploma in Computer Engineering [a game] using Java</p>
          </div>
          <div>
            <h3>Smarter Keyboard Input Method</h3>
            <p>Made as a part of my Bachelor of Computer Engineering Project</p>
          </div>
        </div>
        <div>
          <h2>Legend of points (Does not accurately map to the skills to be used just for reference)</h2>
          <div>
            <ol>
              <li>Heard of it</li>
              <li>Done a <code>Hello World</code> program or something similar</li>
              <li>Done a complete getting started tutorial</li>
              <li>Infrequent user (less than once per quarter)</li>
              <li>Frequent user (more than once a quarter)</li>
              <li>Understands good enough to teach it</li>
              <li>Can understand and discuss it's internal working</li>
              <li>Have contribute a major change to the source code</li>
            </ol>
          </div>
        </div>
      </div>
    </Card>
  </MuiThemeProvider>
)
