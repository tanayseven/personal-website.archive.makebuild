module.exports = {
  bail: true,
  verbose: true,
  coverageReporters: ['json', 'lcov', 'text'],
  collectCoverage: true,
  collectCoverageFrom: [
    '**/*.{js,jsx}',
    '!**/node_modules/**',
    '!**/vendor/**',
  ]
}