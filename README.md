# Personal Reddit Reader

A small personal, non-commercial, read-only Python utility for retrieving
publicly available Reddit posts and comments through the Reddit Data API.

## Purpose

This project is intended for personal learning and experimentation with
Python and Reddit's API.

The application:

- searches publicly available Reddit posts using keywords;
- retrieves basic public post metadata;
- retrieves publicly available comments from selected posts;
- operates in read-only mode;
- does not post, comment, vote, send messages, or interact with users;
- does not perform user profiling;
- does not use Reddit data for AI model training;
- does not sell or redistribute Reddit data.

## Authentication

API credentials are provided using environment variables and are not stored
in this repository.

Required variables:

- REDDIT_CLIENT_ID
- REDDIT_CLIENT_SECRET

## Status

This project is currently awaiting Reddit Data API access approval.
