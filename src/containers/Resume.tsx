import React from 'react'
import { technologySpecificSkills, nonTechnologySpecificSkills, Skills } from '../content/resume'

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

export default () => (
  <div>
    <div>
      {renderSkills(technologySpecificSkills)}
    </div>
    <div>
      {renderSkills(nonTechnologySpecificSkills)}
    </div>
  </div>
)

