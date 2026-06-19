# Event Bus

## Purpose
FounderOS must react to events.

## Prime Directive
Everything is an event.

## Event Sources
User, Files, Projects, Git, Calendar, Email, Research, Competitors, Scheduler, System.

## Event Structure
EVENT_ID, TIMESTAMP, SOURCE, TYPE, PAYLOAD, PRIORITY (Low/Medium/High/Critical), STATUS.

## Event Lifecycle
Detected → Queued → Processed → Logged → Archived.

## Event Types
NEW_PROJECT, FILE_CHANGED, REPOSITORY_UPDATED, COMPETITOR_EVENT, RESEARCH_EVENT, TASK_DUE, MISSION_UPDATE, NEW_IDEA, DECISION_REQUEST.

## Routing Rule
Events routed to: Decision Engine, Project Monitor, Watchtower, Automation Engine, Knowledge Engine.
