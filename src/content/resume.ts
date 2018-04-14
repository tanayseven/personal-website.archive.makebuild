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

export { technologySpecificSkills, nonTechnologySpecificSkills, Skills }