interface Skill {
  name: string,
  points: number,
}

interface Skills extends Array<Skill>{}

const technologySpecificSkills: Skills = [
  {
    name: 'Python',
    points: 7,
  },
  {
    name: 'Flask - Python',
    points: 6,
  },
  {
    name: 'Django - Python',
    points: 3,
  },
  {
    name: 'Docker',
    points: 4,
  },
  {
    name: 'Java',
    points: 7,
  },
  {
    name: 'Native Android',
    points: 3,
  },
  {
    name: 'Javascript',
    points: 5,
  },
  {
    name: 'Clojure',
    points: 4,
  },
  {
    name: 'HTML/CSS',
    points: 6,
  },
  {
    name: 'SQL',
    points: 5,
  },
]

const nonTechnologySpecificSkills: Skills = [
  {
    name: 'Test Driven Development',
    points: 6.5,
  },
  {
    name: 'Web Based Software Development',
    points: 6,
  },
  {
    name: 'Follow Scrum in Software Development',
    points: 5,
  },
  {
    name: 'Learning a new language/technology',
    points: 6,
  },
  {
    name: 'Structured Programming',
    points: 7,
  },
  {
    name: 'Object Oriented Programming',
    points: 6,
  },
  {
    name: 'Functional Programming',
    points: 5,
  },
]

interface WorkExperience {
  company: string,
  position: string,
  timePeriod: string,
  details: string,
}

interface WorkExperienceList extends Array<WorkExperience>{}

const workExperienceList: WorkExperienceList = [
  {
    company: 'Tata Consultancy Services',
    position: 'Intern',
    timePeriod: 'December 2013 to January 2014',
    details: 'Worked on profiling an embedded application written for Windows Embedded Standard 7 Technology used to develop was C# and profilers used were Red Gate ANTS and CLR',
  },
  {
    company: 'Nelkinda Software Craft',
    position: 'Intern',
    timePeriod: 'December 2013 to January 2014',
    details: 'Worked on profiling an embedded application written for Windows Embedded Standard 7 Technology used to develop was C# and profilers used were Red Gate ANTS and CLR',
  },
]

interface KeyHighlight {
    icon: string,
    topic: string,
    description: string,
}

interface KeyHighlights extends Array<KeyHighlight>{}

const keyHighlights: KeyHighlights = [
    {
        icon: 'code.svg',
        topic: 'Programmer by heart and by soul',
        description: 'Something I love doing a lot not just professionally but also as a hobby is programming. It gives me a lot of joy and a sandbox for my creative mind.',
    },
    {
        icon: 'python.svg',
        topic: 'Python Programming Language',
        description: 'Python is the language that I know the most and have done lot of development in it.',
    },
    {
        icon: 'sticky-note.svg',
        topic: 'Problem Solving/Consulting',
        description: 'I love solving challenging problems using software and even more solving a problem collaboratively in a group.',
    },
    {
        icon: 'vial.svg',
        topic: 'Testing and Test Driven Development',
        description: 'I have a preference towards driving a software projects using tests and make it as robust and foolproof as possible.',
    },
    {
        icon: 'globe.svg',
        topic: 'Web Development',
        description: 'The one technical domain that I am well worse with is Web Development and know the deep internals of it.',
    },
]

export { 
  technologySpecificSkills,
  nonTechnologySpecificSkills,
  workExperienceList,
  keyHighlights,
  Skills,
  WorkExperience,
  KeyHighlights,
}
