import React from 'react'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import Card from 'material-ui/Card'
import Chip from 'material-ui/Chip'
import Typography from 'material-ui/Typography'
import theme from '../components/theme'

const resumeData = {
  nonTechSpecificSkills: [
    {name: 'Test Driven Development', points: '6.5'},
    {name: 'Web based software development', points: 6},
    {name: 'Follow scrum in software development', points: 5},
    {name: 'Learning a new language/technology stars', points: 6},
    {name: 'Structured Programming', points: 7},
    {name: 'Object Oriented Programming', points: 6},
    {name: 'Functional Programming', points: 5},
  ],
  techSpecificSkills: [
    {name: 'Python', points: 7},
    {name: 'Flask - Python', points: 6},
    {name: 'Django - Python', points: 3},
    {name: 'Docker', points: 3},
    {name: 'Java', points: 5},
    {name: 'Django - Python', points: 3},
    {name: 'Docker', points: 3},
    {name: 'Java', points: 5},
    {name: 'Native Android', points: 5},
    {name: 'JavaScript', points: 5},
    {name: 'Clojure', points: 4},
    {name: 'HTML/CSS', points: 6},
    {name: 'SQL', points: 5},
  ]
}

export default () => (
  <MuiThemeProvider theme={theme}>
    <Card style={{padding: '10px'}}>
      <Typography type='heading'>
        Skills (Non technology specific)
      </Typography>
      {resumeData.nonTechSpecificSkills.map((skill) =>
        <Chip
          label={skill.name}
          deleteIcon={<p>{skill.points}</p>}
          style={{margin: '3px'}}
          onDelete={()=>{}} />)
      }
    </Card>
    <br />
    <Card style={{padding: '10px'}}>
      <Typography type='heading'>
        Skills (Language/Technology)
      </Typography>
      {resumeData.techSpecificSkills.map((skill) =>
        <Chip
          label={skill.name}
          deleteIcon={<Avatar>{skill.points}</Avatar>}
          style={{margin: '3px'}}
          onDelete={()=>{}} />)
      }
    </Card>
    <br />
    <h2>Work Experience</h2>
    <Card style={{padding: '10px'}}>
      <h3>Internship at Tata Consultancy Services</h3>
      <p>December 2013 to January 2014</p>
      <ul>
        <li>Worked on profiling an embedded application written for Windows Embedded Standard 7</li>
        <li>Technology used to develop was C# and profilers used were Red Gate ANTS and CLR</li>
      </ul>
    </Card>
    <br />
    <Card style={{padding: '10px'}}>
      <h3>Software Craftsman at Nelkinda Software Craft</h3>
      <p>September 2016 to 2017</p>
      <ul>
        <li>Working on project that include Flask - Python and Native Android - Java development</li>
        <li>Daily use of practices like scrum and TDD in the software development process</li>
      </ul>
    </Card>
    <br />
    <br />
    <h2>Personal Projects</h2>
    <Card style={{padding: '10px'}}>
      <h3>Pitchy Bird</h3>
      <p>A browser based Flappy Bird inspired game controlled by using voice</p>
    </Card>
    <br />
    <Card style={{padding: '10px'}}>
      <h3>JTankWars</h3>
      <p>Made as a part of my final project for Diploma in Computer Engineering [a game] using Java</p>
    </Card>
    <br />
    <Card style={{padding: '10px'}}>
      <h3>Smarter Keyboard Input Method</h3>
      <p>Made as a part of my Bachelor of Computer Engineering Project</p>
    </Card>
    <br />
    <br />
    <Card style={{padding: '10px'}}>
      <h2>Legend of points (Does not accurately map to the skills to be used just for reference)</h2>
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
    </Card>
  </MuiThemeProvider>
)
