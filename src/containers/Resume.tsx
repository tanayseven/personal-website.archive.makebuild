import React from 'react'
import { technologySpecificSkills, nonTechnologySpecificSkills, workExperienceList, Skills, WorkExperience } from '../content/resume'

function renderSkills(skills: Skills) {
  return (
    <div className="collection">
    {skills.map((skill)=>(
      <a href="#!" className="collection-item">
      <span className="new badge" data-badge-caption=" / 8">
        {skill.points}
      </span>
      {skill.name}
      </a>
    ))}
    </div>
  )
}

function renderWorkExperience(workExperience: WorkExperience) {
  return (
    <div className="card">
      <div className="card-content">
        <span className="card-title black-text text-darken-4">{workExperience.company}</span>
        <h6>{workExperience.position}</h6>
        <p className="grey-text">{workExperience.timePeriod}</p>
        <p>{workExperience.details}</p>
      </div>
    </div>
  )
}

export default () => (
  <div>
    <h4>Key Highlights</h4>
    <div>
      {/* TODO add key highlights */}
    </div>
    <h4>Skills</h4>
    <div>
      {renderSkills(technologySpecificSkills)}
    </div>
    <div>
      {renderSkills(nonTechnologySpecificSkills)}
    </div>
    <h4>Work Experience</h4>
    {workExperienceList.map((workExperience) => (
      renderWorkExperience(workExperience)
    ))}
    <h4>Personal Projects</h4>
    <div>
      {/* TODO add personal projects here */}
    </div>
    <h4>Legend</h4>
    <div>
      {/* TODO add legend here */}
    </div>
  </div>
)

