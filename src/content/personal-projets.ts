interface PersonalProject {
  title: string,
  description: string,
  liveLink: string|null,
  codeLink: string|null,
  image: string|null,
}

interface PersonalProjects extends Array<PersonalProject>{};

const personalProjects: PersonalProjects = [
  {
    title: 'Pitchy Bird',
    description: 'A voice controlled browser based game simillar to flappy bird',
    liveLink: 'https://pitchybird.herokuapp.com',
    codeLink: 'https://github.com/tanayseven/PitchyBird',
    image: '/images/project_thumbs/pitchy_bird.png',
  },
  {
    title: 'SKIM (Sentence completion and prediction)',
    description: 'BE final year research based project to aid in typing on computers',
    liveLink: 'https://link.springer.com/chapter/10.1007/978-3-319-11933-5_43',
    codeLink: null,
    image: '/images/project_thumbs/skim.png',
  },
  {
    title: 'Techyon 2013',
    description: 'This is not so very long project description',
    liveLink: 'http://tanayseven.github.io/techyon2013/',
    codeLink: 'https://github.com/tanayseven/techyon2013',
    image: '/images/project_thumbs/techyon.png',
  },
  {
    title: 'JTankWars',
    description: 'My very fist project a 2d game in Java a clone of Battle City',
    codeLink: 'https://github.com/tanayseven/j-tank-wars',
    liveLink: null,
    image: null,
  },
  {
    title: 'Find Figam',
    description: 'A app hacked over a night and refined over time for a hackathon code for cause',
    liveLink: 'http://www.hackathon.io/find-figam',
    codeLink: null,
    image: '/images/project_thumbs/find_figam.png'
  },
  {
    title: 'Chatoodle',
    description: 'A socket.io based web app to chat and doodle at the same time',
    liveLink: 'https://chatoodle.herokuapp.com/',
    codeLink: 'https://github.com/tanayseven/Chatoodle',
    image: '/images/project_thumbs/chatoodle.png',
  },
  {
    title: 'Voix Twitter',
    description: 'An online polling app that uses twitter to accept votes and casts them',
    liveLink: null,
    codeLink: 'https://github.com/tanayseven/voix-twitter',
    image: null,
  },
  {
    title: 'SMS Server',
    description: 'An Android app that accepts registrations and votes via SMSes',
    liveLink: 'https://drive.google.com/file/d/0B8ZGvtCVIoJgNlZPMnU3WHVXcFk/view',
    codeLink: null,
    image: null,
  },
]

export default personalProjects