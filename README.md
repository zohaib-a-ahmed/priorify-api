# Backend for Priorify

Priorify is a productivity manager designed for myself and my peers that allows users to keep track of upcoming events as well as assignments related to school. It incoporates Google's Gemini Pro LLM for convenience in creating and managing a user's stored calendar and assignments.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)

## Getting Started

- You can create an account with Google and sign in [here](https://priorify.onrender.com).
- The application API is deployed and hosted via [Render](https://render.com/).
  - Note: This is hosted freely, and consequently might take a few minutes to re-spin up deployment.

## Usage

If the application is taking a while to spin up, check out this usage video [here](https://youtu.be/AAtQp4UJdOo)

## Features

- Calendar management allows users to create and store items and keep track of upcoming events and assignments
- Google Gemini Integration allows users to bypass manually creating events/assignments, and utilize natural language to command a secretary to do so.

## Technologies Used

The application is built within the NextJS framework, utilizing Mantine and TailwindCSS for UI styling. It queries a RESTful API made with Flask that manages a PostgreSQL database located [here](https://github.com/zohaib-a-ahmed/priorify-api)
