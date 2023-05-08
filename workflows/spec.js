#!/usr/bin/env javascript

describe('My First Test', () => {
	  it('Visits the Cypress homepage', () => {
		      cy.visit('https://www.cypress.io')
		      cy.contains('Start building').click()
		      cy.url().should('include', '/guide/getting-started/introduction')
		    })
})
