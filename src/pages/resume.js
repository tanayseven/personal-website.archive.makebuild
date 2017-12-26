import React from "react";
import Page from "../components/page";

export default () => {
    return (
      <Page
      content={
        <div>
          <div class="skills-list resume-section">
              <h2>Skills (Non technology specific)</h2>
              <div class="skill-item">Test Driven Software Development (6.5)</div>
              <div class="skill-item">Web based software development (6) </div>
              <div class="skill-item">Follow scrum in software development (5)</div>
              <div class="skill-item">Learning a new language/technology stars(6)</div>
              <div class="skill-item">Structured Programming (7)</div>
              <div class="skill-item">Object Oriented Programming (6)</div>
              <div class="skill-item">Functional Programming stars(5)</div>
          </div>
          <div class="skills-list resume-section">
              <h2>Skills (Language/Technology)</h2>
              <div class="skill-item">Python (7)</div>
              <div class="skill-item">Flask - Python (6)</div>
              <div class="skill-item">Django - Python (3)</div>
              <div class="skill-item">Docker (3)</div>
              <div class="skill-item">Java (5)</div>
              <div class="skill-item">Native Android (5)</div>
              <div class="skill-item">JavaScript (5)</div>
              <div class="skill-item">Clojure (4)</div>
              <div class="skill-item">HTML/CSS (6)</div>
              <div class="skill-item">SQL (5)</div>
          </div>
          <div class="skills-list resume-section"></div>
          <div class="resume-section">
              <h2>Work Experience</h2>
              <div class="resume-sub-section">
                  <h3>Internship at Tata Consultancy Services</h3>
                  <p>December 2013 to January 2014</p>
                  <ul>
                      <li>Worked on profiling an embedded application written for Windows Embedded Standard 7</li>
                      <li>Technology used to develop was C# and profilers used were Red Gate ANTS and CLR</li>
                  </ul>
              </div>
              <div class="resume-sub-section">
                  <h3>Software Craftsman at Nelkinda Software Craft</h3>
                  <p>September 2016 to 2017</p>
                  <ul>
                      <li>Working on project that include Flask - Python and Native Android - Java development</li>
                      <li>Daily use of practices like scrum and TDD in the software development process</li>
                  </ul>
              </div>
          </div>
          <div class="resume-section">
              <h2>Personal Projects</h2>
              <div class="resume-sub-section">
                  <h3>Pitchy Bird</h3>
                  <p>A browser based Flappy Bird inspired game controlled by using voice</p>
              </div>
              <div class="resume-sub-section">
                  <h3>JTankWars</h3>
                  <p>Made as a part of my final project for Diploma in Computer Engineering [a game] using Java</p>
              </div>
              <div class="resume-sub-section">
                  <h3>Smarter Keyboard Input Method</h3>
                  <p>Made as a part of my Bachelor of Computer Engineering Project</p>
              </div>
          </div>
          <div class="resume-section">
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
      }/>
    )
}
