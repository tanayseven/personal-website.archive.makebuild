import React from 'react'
import { withSiteData } from 'react-static'
import SocialSiteLink from '../compoents/social-site-buttons'
import ProjectCard from "../compoents/project-card";
import personalProjects from "../content/personal-projets"

export default withSiteData(() => (
  [
    <div>
      <SocialSiteLink icon="linkedin" colour="light-blue darken-3" link="https://www.linkedin.com/in/tanay-prabhudesai"/>
      <SocialSiteLink icon="twitter" colour="light-blue accent-4" link="https://twitter.com/tanayseven"/>
      <SocialSiteLink icon="github" colour="grey darken-4" link="https://github.com/tanayseven/"/>
      <SocialSiteLink icon="gitlab" colour="deep-orange accent-2" link="https://gitlab.com/tanayseven"/>
      <div>
      {personalProjects.map((project)=>(
        <ProjectCard
            title={project.title}
            image={project.image}
            liveLink={project.liveLink}
            codeLink={project.codeLink}
        >
            {project.description}
        </ProjectCard>
      ))}
      </div>
    </div>
    ]
))
