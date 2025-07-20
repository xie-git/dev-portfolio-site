#!/usr/bin/env python3
"""
Simple Portfolio Website - Main Application File
"""

import os
from flask import Flask, render_template_string, send_from_directory, send_file

def create_app():
    """Creates and configures the Flask application."""
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

    # All of your project data and HTML templates go here, inside the create_app function
    home_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Michael Xie - Software Engineer</title>
        <meta name="description" content="Michael Xie is a software engineer specializing in big data ETL pipelines, cloud infrastructure, and scalable systems. 5+ years experience in fintech and enterprise software.">
        <meta name="keywords" content="Michael Xie, Software Engineer, Python, AWS, Data Engineering, ETL, Cloud Infrastructure, Chicago">
        <meta name="author" content="Michael Xie">
        
        <!-- Open Graph / Facebook -->
        <meta property="og:type" content="website">
        <meta property="og:title" content="Michael Xie - Software Engineer">
        <meta property="og:description" content="Software engineer specializing in big data ETL pipelines, cloud infrastructure, and scalable systems.">
        <meta property="og:url" content="https://micheal-xie.dev">
        
        <!-- Twitter -->
        <meta property="twitter:card" content="summary">
        <meta property="twitter:title" content="Michael Xie - Software Engineer">
        <meta property="twitter:description" content="Software engineer specializing in big data ETL pipelines, cloud infrastructure, and scalable systems.">
        
        <!-- Favicon -->
        <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
        
        <!-- Preload fonts for better performance -->
        <link rel="preload" href="/static/fonts/PPNeueMontreal-Regular.woff" as="font" type="font/woff" crossorigin>
        <link rel="preload" href="/static/fonts/PPNeueMontreal-Italic.woff" as="font" type="font/woff" crossorigin>
        
        <style>
            /* EXACT Long Nguyen Font Loading - LOCAL HOSTING */
            @font-face {
                font-family: 'PP Neue Montreal';
                src: url('/static/fonts/PPNeueMontreal-Regular.woff') format("woff");
                font-weight: 400;
                font-style: normal;
                font-display: swap;
            }

            @font-face {
                font-family: 'PP Neue Montreal';
                src: url('/static/fonts/PPNeueMontreal-Italic.woff') format("woff");
                font-weight: 400;
                font-style: italic;
                font-display: swap;
            }
            
            /* Ensure immediate font loading for critical text */
            html {
                font-family: 'PP Neue Montreal', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            }

            /* EXACT Long Nguyen CSS Variables */
            :root {
                --color-bg-main: #fffbfc;
                --color-fg-main: #4a3847;
                --spacing-xs: .25rem;
                --spacing-sm: .5rem;
                --spacing-md: 1.5rem;
                --spacing-lg: 2rem;
                --spacing-xl: 3rem;
                --spacing-xxl: 4rem;
            }
            
            /* EXACT Long Nguyen Base Styles */
            * {
                box-sizing: border-box;
            }
            
            body {
                position: relative;
                min-height: calc(100vh - env(safe-area-inset-bottom));
                margin: 0;
                padding: env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left);
                display: flex;
                flex-flow: column nowrap;
                font: 1.5rem 'PP Neue Montreal', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
                color: var(--color-fg-main);
                background: var(--color-bg-main);
            }

            body > * {
                flex: 1 0 auto;
            }
            
            /* EXACT Long Nguyen Typography */
            h1, h2, h3, h4, h5, h6 {
                margin: 0;
                font-size: 1.5rem;
                font-weight: 400;
            }

            h1 {
                font-size: 1.8rem;
                text-transform: none;
                font-weight: 400;
            }

            button {
                border: 0;
                background: none;
                padding: 0;
            }

            a {
                color: inherit;
                text-decoration: underline;
            }
            
            /* Remove underline from contact links */
            .links-list a[href="#contact"] {
                text-decoration: none;
            }
            
            .links-list a[href="#contact"]:hover {
                text-decoration: none;
            }

            code {
                background: rgba(45, 23, 36, .1);
                padding: .05em .25em .1em;
            }

            a:visited {
                color: inherit;
            }

            /* EXACT Long Nguyen Utility Classes */
            .block {
                margin: auto;
                width: 100%;
                max-width: 66ch;
            }
            
            .flex {
                display: flex;
            }
            
            .flex-grow {
                flex: 1 0 auto;
            }
            
            .flex-columns {
                flex-direction: column;
            }
            
            .flex-nowrap {
                flex-wrap: nowrap;
            }

            /* EXACT Long Nguyen Container System */
            .container {
                position: relative;
                --spacing-vertical: 0;
                --spacing-horizontal: 0;
                --configuration: var(--spacing-vertical) var(--spacing-horizontal);
            }

            .horizontal {
                --spacing-horizontal: var(--spacing-md);
            }

            .padding {
                padding: var(--configuration);
            }

            .margin {
                margin: var(--configuration);
            }
            
            /* EXACT Long Nguyen Header */
            header {
                background: var(--color-bg-main);
                position: sticky;
                bottom: 0;
                order: 2;
                z-index: 10;
            }

            header h2 {
                font-size: 1.5rem;
                font-weight: 400;
                margin: 0 auto 0 0;
                font-family: inherit;
            }

            nav {
                position: relative;
            }

            .container-actions {
                padding: var(--spacing-md) 0;
                display: flex;
                flex-flow: row nowrap;
            }

            header ul {
                margin: 0;
                padding: 0;
            }

            header li {
                list-style: none;
                margin: 0 var(--spacing-sm);
            }

            .links-container {
                display: flex;
                flex-flow: row nowrap;
                align-items: flex-end;
            }

            .links-list {
                display: flex;
                align-items: flex-end;
            }

            .container-actions .links-list {
                flex-flow: row nowrap;
            }
            
            /* EXACT Long Nguyen Content Styles */
            .intro-container p {
                margin-bottom: var(--spacing-md);
                max-width: 512px;
            }

            .intro-container {
                display: grid;
                grid-template-columns: 1fr 1fr;
                column-gap: var(--spacing-xl);
                align-items: start;
            }
            
            .intro-left p {
                margin: 0;
            }
            
            .intro-right {
                text-align: right;
            }
            
            .intro-container ul {
                padding: 0;
                list-style: none;
                margin: 0;
            }

            .intro-container {
                margin-top: var(--spacing-xxl);
                margin-bottom: 6rem;
            }

            /* EXACT Long Nguyen Works Section */
            .works-section {
                margin: 4.5rem auto;
            }

            .works-section h2 {
                font-weight: 400;
                font-size: 1rem;
                text-transform: uppercase;
                margin: var(--spacing-md) auto;
            }

            /* EXACT Long Nguyen Project Cards */
            .project-card h3 {
                font-weight: 400;
                font-size: 1rem;
                text-transform: uppercase;
                margin: 0;
            }

            .project-card p {
                font-size: 0.875rem;
                opacity: .5;
                margin: 0;
            }

            .project-card img {
                aspect-ratio: 3 / 2;
                object-fit: cover;
                width: 100%;
                border: 1px solid var(--color-fg-main);
            }

            .project-card {
                display: flex;
                flex-flow: column nowrap;
                row-gap: var(--spacing-sm);
                margin: var(--spacing-sm) auto;
                width: 100%;
            }

            .project-card .fade {
                opacity: 50%;
            }

            .project-placeholder {
                aspect-ratio: 3 / 2;
                width: 100%;
                border: 1px solid var(--color-fg-main);
                background: #f5f5f5;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 2rem;
                color: var(--color-fg-main);
                opacity: 0.3;
            }

            .project-image {
                aspect-ratio: 3 / 2;
                width: 100%;
                border: 1px solid var(--color-fg-main);
                object-fit: cover;
                transition: transform 0.3s ease;
            }

            .project-card {
                cursor: pointer;
                transition: transform 0.2s ease;
            }

            .project-card:hover {
                transform: translateY(-2px);
            }

            /* See All Projects Link */
            .see-all-container {
                text-align: right;
                margin-top: var(--spacing-lg);
            }

            .see-all-link {
                color: var(--color-fg-main);
                text-decoration: none;
                font-size: 0.875rem;
                opacity: 0.6;
                transition: opacity 0.3s ease;
            }

            .see-all-link:hover {
                opacity: 1;
                text-decoration: underline;
            }

            /* Modal Styles - Ultra Minimal & Centered */
            .modal {
                display: none;
                position: fixed;
                z-index: 1000;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                background: rgba(45, 23, 36, 0.8);
                align-items: center;
                justify-content: center;
            }

            .modal.show {
                display: flex;
            }

            .modal-content {
                background: var(--color-bg-main);
                border: 1px solid var(--color-fg-main);
                width: 90%;
                max-width: 1200px;
                height: 70vh;
                position: relative;
                display: grid;
                grid-template-columns: 1fr 1fr;
            }

            .modal-left {
                padding: var(--spacing-xxl);
                display: flex;
                flex-direction: column;
            }

            .modal-right {
                padding: var(--spacing-xxl);
                display: flex;
                flex-direction: column;
                gap: var(--spacing-lg);
            }

            .modal-header {
                margin-bottom: var(--spacing-lg);
            }

            .modal-title {
                font-size: 1.1rem;
                margin: 0;
                text-transform: uppercase;
                font-weight: 600;
            }

            .modal-type {
                opacity: 0.5;
                font-size: 0.8rem;
                margin-top: var(--spacing-xs);
                font-weight: 400;
            }

            .close {
                position: absolute;
                right: var(--spacing-lg);
                top: var(--spacing-lg);
                font-size: 1.2rem;
                cursor: pointer;
                line-height: 1;
                color: var(--color-fg-main);
                font-weight: 400;
            }

            .close:hover {
                opacity: 0.7;
            }

            .modal-image {
                aspect-ratio: 4 / 3;
                width: 100%;
                border: 1px solid var(--color-fg-main);
                background: #f5f5f5;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 6rem;
                color: var(--color-fg-main);
                opacity: 1;
                flex-grow: 1;
                overflow: hidden;
            }

            .modal-overview {
                font-size: 0.8rem;
                line-height: 1.4;
                opacity: 0.7;
                margin-top: var(--spacing-md);
                font-weight: 400;
            }

            .modal-section {
                margin-bottom: var(--spacing-md);
            }

            .modal-section h3 {
                font-size: 0.8rem;
                text-transform: uppercase;
                margin-bottom: var(--spacing-sm);
                color: var(--color-fg-main);
                font-weight: 600;
                letter-spacing: 0.1em;
            }

            .modal-section p {
                font-size: 0.8rem;
                line-height: 1.4;
                margin: 0;
                color: var(--color-fg-main);
                font-weight: 400;
            }

            .tech-list {
                display: flex;
                flex-wrap: wrap;
                gap: var(--spacing-sm);
            }

            .tech-tag {
                font-size: 0.75rem;
                color: var(--color-fg-main);
                font-weight: 400;
            }

            .tech-tag:not(:last-child)::after {
                content: "•";
                margin-left: var(--spacing-sm);
                opacity: 0.5;
            }

            .feature-list {
                list-style: none;
                padding: 0;
                margin: 0;
                font-size: 0.75rem;
            }

            .feature-list li {
                padding: 0.15rem 0;
                color: var(--color-fg-main);
                line-height: 1.4;
                font-weight: 400;
            }

            /* Mobile responsive for modal */
            @media (max-width: 768px) {
                .modal-content {
                    grid-template-columns: 1fr;
                    width: 95%;
                    height: 85vh;
                }

                .modal-left {
                    padding: var(--spacing-lg);
                }

                .modal-right {
                    padding: var(--spacing-lg);
                    gap: var(--spacing-md);
                }

                .modal-image {
                    aspect-ratio: 3 / 2;
                    font-size: 4rem;
                }
            }
            
            /* Developer Story Timeline - Reference Image Style */
            .developer-story-section {
                margin: 4.5rem auto;
            }

            .developer-story-section h2 {
                font-weight: 400;
                font-size: 1rem;
                text-transform: uppercase;
                margin: var(--spacing-md) auto var(--spacing-xxl) auto;
            }

            .timeline-wrapper {
                position: relative;
                margin-top: var(--spacing-xxl);
                max-width: 900px;
                margin-left: auto;
                margin-right: auto;
                padding: 0 var(--spacing-lg);
            }

            /* Central timeline line */
            .timeline-wrapper::before {
                content: '';
                position: absolute;
                left: 50%;
                top: 0;
                bottom: 0;
                width: 1px;
                background: rgba(74, 74, 74, 0.3);
                transform: translateX(-50%);
                z-index: 1;
            }

            .timeline-item {
                position: relative;
                margin-bottom: 4rem;
                display: flex;
                width: 100%;
            }

            /* Alternating layout - FIXED positioning */
            .timeline-item:nth-child(odd) {
                justify-content: flex-start;
            }

            .timeline-item:nth-child(even) {
                justify-content: flex-end;
            }

            .timeline-content {
                width: 45%;
                max-width: 380px;
                padding: var(--spacing-lg);
                border: 1px solid var(--color-fg-main);
                position: relative;
                background: var(--color-bg-main);
                display: flex;
                gap: var(--spacing-md);
                transition: all 0.3s ease;
            }

            .timeline-content:hover {
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                transform: translateY(-2px);
            }

            /* Timeline arrows */
            .timeline-content::before {
                content: '';
                position: absolute;
                top: var(--spacing-lg);
                width: 0;
                height: 0;
                border-style: solid;
            }

            /* Left-aligned items (odd) - arrow points right */
            .timeline-item:nth-child(odd) .timeline-content::before {
                right: -8px;
                border-width: 8px 0 8px 8px;
                border-color: transparent transparent transparent var(--color-fg-main);
            }

            /* Right-aligned items (even) - arrow points left */
            .timeline-item:nth-child(even) .timeline-content::before {
                left: -8px;
                border-width: 8px 8px 8px 0;
                border-color: transparent var(--color-fg-main) transparent transparent;
            }

            /* Remove central marker circles */

            /* Large company logo on left */
            .company-logo-large {
                width: 48px;
                height: 48px;
                object-fit: contain;
                flex-shrink: 0;
                opacity: 0.9;
            }

            /* Content area next to logo */
            .timeline-text-content {
                flex: 1;
                position: relative;
            }

            /* Tag in top right corner */
            .timeline-type {
                position: absolute;
                top: 0;
                right: 0;
                font-size: 0.6rem;
                text-transform: uppercase;
                padding: 0.15rem 0.4rem;
                border-radius: 10px;
                font-weight: 500;
                letter-spacing: 0.05em;
                color: white;
            }

            .timeline-type.education {
                background: #6b6b6b;
            }

            .timeline-type.work {
                background: #8a8a8a;
            }

            .timeline-type.project {
                background: #5a7a8a;
            }

            /* Date styling */
            .timeline-date {
                font-size: 0.75rem;
                opacity: 0.6;
                letter-spacing: 0.05em;
                margin-bottom: var(--spacing-xs);
                margin-top: var(--spacing-sm);
            }

            /* Company-branded job titles */
            .timeline-content h3 {
                font-size: 0.95rem;
                font-weight: 400;
                margin: 0 0 var(--spacing-xs) 0;
                line-height: 1.2;
            }

            .timeline-content h3.northern-trust {
                color: #4a7c59;
            }

            .timeline-content h3.capital-one {
                color: #b85450; /* Desaturated Capital One Red */
            }

            .timeline-content h3.northwestern-mutual {
                color: #4a5566; /* Desaturated Northwestern Mutual Navy */
            }

            .timeline-content h3.education {
                color: #4a4a4a; /* Desaturated Black for education */
            }

            /* Company name styling */
            .timeline-company {
                font-size: 0.85rem;
                opacity: 0.7;
                margin-bottom: var(--spacing-sm);
                font-weight: 400;
                letter-spacing: 0.01em;
            }

            .timeline-content p {
                font-size: 0.875rem;
                line-height: 1.4;
                opacity: 0.7;
                margin: 0;
                letter-spacing: 0.01em;
            }

            /* Remove old company styling */
            .company-logo {
                display: none;
            }

            /* Resume page specific styles */
            .resume-list {
                display: flex;
                flex-direction: column;
                gap: var(--spacing-md);
                margin: 0;
                padding: 0;
                list-style: none;
            }
            
            .resume-list-item {
                padding-bottom: var(--spacing-sm);
            }
            
            .resume-item-header {
                margin-bottom: var(--spacing-sm);
            }
            
            .resume-item-title {
                font-size: 0.875rem;
                font-weight: 500;
                margin: 0 0 var(--spacing-sm) 0;
                color: var(--color-fg-main);
                letter-spacing: 0.01em;
            }
            
            .resume-item-company {
                font-size: 0.875rem;
                opacity: 0.7;
                margin: 0 0 var(--spacing-sm) 0;
                letter-spacing: 0.01em;
            }
            
            .resume-item-date {
                font-size: 0.75rem;
                opacity: 0.6;
                text-transform: uppercase;
                letter-spacing: 0.02em;
                margin: 0;
            }
            
            .resume-item-details {
                margin: var(--spacing-sm) 0 0 0;
                padding: 0;
                list-style: none;
            }
            
            .resume-item-details li {
                font-size: 0.875rem;
                line-height: 1.4;
                opacity: 0.8;
                margin-bottom: var(--spacing-xs);
                padding-left: var(--spacing-sm);
                position: relative;
                letter-spacing: 0.01em;
            }
            
            .resume-item-details li::before {
                content: '•';
                position: absolute;
                left: 0;
                color: rgba(74, 74, 74, 0.5);
            }
            
            /* Resume page letter spacing for non-headers */
            .resume-item-company,
            .resume-item-date {
                letter-spacing: 0.01em;
            }
            
            /* Hide timeline for education section */
            .education-section .timeline-wrapper::before {
                display: none;
            }
            
            .education-section .timeline-item .timeline-marker {
                display: none;
            }
            
            /* Skills section styling */
            .skills-content {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: var(--spacing-xl);
            }
            
            .skill-category {
                padding-bottom: var(--spacing-md);
                border-bottom: 1px solid rgba(74, 74, 74, 0.1);
            }
            
            .skill-category:last-child,
            .skill-category:nth-last-child(2) {
                border-bottom: none;
            }
            
            @media (max-width: 768px) {
                .skills-content {
                    grid-template-columns: 1fr;
                }
                
                .skill-category:nth-last-child(2) {
                    border-bottom: 1px solid rgba(74, 74, 74, 0.1);
                }
            }
            
            .skill-category h3 {
                font-size: 0.875rem;
                font-weight: 500;
                margin: 0 0 var(--spacing-xs) 0;
                color: var(--color-fg-main);
                text-transform: uppercase;
                letter-spacing: 0.02em;
            }
            
            .skill-category p {
                font-size: 0.875rem;
                line-height: 1.5;
                opacity: 0.8;
                margin: 0;
                letter-spacing: 0.01em;
            }
            
            /* Certifications section styling */
            .certifications-content {
                display: flex;
                flex-direction: column;
                gap: var(--spacing-md);
            }
            
            .certification-category {
                padding-bottom: var(--spacing-sm);
                border-bottom: 1px solid rgba(74, 74, 74, 0.1);
            }
            
            .certification-category:last-child {
                border-bottom: none;
            }
            
            .certification-category h3 {
                font-size: 0.875rem;
                font-weight: 500;
                margin: 0 0 var(--spacing-xs) 0;
                color: var(--color-fg-main);
                text-transform: uppercase;
                letter-spacing: 0.02em;
            }
            
            /* Add space between resume content and footer */
            .resume-page main {
                margin-bottom: calc(var(--spacing-xxl) + 2rem);
            }
            
            /* PDF download link styling */
            .pdf-link-container {
                text-align: right;
                margin: var(--spacing-lg) 0;
                padding: 0 var(--spacing-md);
            }
            
            .pdf-download-link {
                color: var(--color-fg-main);
                text-decoration: none;
                font-size: 0.875rem;
                opacity: 0.7;
                transition: opacity 0.3s ease;
                letter-spacing: 0.01em;
            }
            
            .pdf-download-link:hover {
                opacity: 1;
                text-decoration: underline;
            }
            
            /* Resume page back link styling */
            .resume-header {
                margin-bottom: var(--spacing-lg);
            }
            
            .resume-header .back-link {
                display: inline-block;
                color: var(--color-fg-main);
                text-decoration: none;
                font-size: 0.875rem;
                opacity: 0.6;
                transition: opacity 0.3s ease;
            }
            
            .resume-header .back-link:hover {
                opacity: 1;
                text-decoration: underline;
            }
            
            /* Resume page section headers - match front page styling */
            .resume-page .wrapper h2 {
                font-weight: 400;
                font-size: 1rem;
                text-transform: uppercase;
                margin: var(--spacing-md) auto var(--spacing-lg) auto;
                cursor: pointer;
                user-select: none;
                transition: opacity 0.3s ease;
            }
            
            .resume-page .wrapper h2:hover {
                opacity: 0.7;
            }
            
            /* Collapsible content */
            .collapsible-content {
                overflow: hidden;
                transition: max-height 0.3s ease;
            }
            
            .collapsible-content.collapsed {
                max-height: 0;
            }
            
            .collapsible-content.expanded {
                max-height: 2000px;
            }
            
            /* Resume page scroll offset for fixed header */
            .resume-page section[id] {
                scroll-margin-top: 100px;
            }

            /* Mobile responsive */
            @media (max-width: 768px) {
                .timeline-wrapper {
                    padding: 0 var(--spacing-md);
                }

                .timeline-wrapper::before {
                    left: 1rem;
                    transform: none;
                }

                .timeline-item,
                .timeline-item:nth-child(even),
                .timeline-item:nth-child(odd) {
                    justify-content: flex-start;
                }

                .timeline-content {
                    width: calc(100% - 3rem);
                    margin-left: var(--spacing-xl);
                }

                .timeline-content::before {
                    display: none;
                }

                .company-logo-large {
                    width: 36px;
                    height: 36px;
                }
            }

            /* EXACT Long Nguyen Statement Section */
            .statement-section {
                margin: 4.5rem auto;
            }
            
            .statement-section .text-lg {
                font-size: 2.5rem;
            }
            
            .statement-section a {
                text-decoration: underline;
            }

            /* EXACT Long Nguyen Footer */
            footer {
                flex-shrink: 0;
            }

            .footer-links h2 {
                font-weight: 400;
                font-size: 0.75rem;
                text-transform: uppercase;
                margin-bottom: var(--spacing-sm);
            }

            .footer-links ul {
                margin: 0;
                margin-top: var(--spacing-sm);
                margin-bottom: var(--spacing-xl);
                padding: 0;
            }

            .footer-links li {
                list-style: none;
                font-size: 1.5rem;
                margin: var(--spacing-sm) auto;
            }

            footer small {
                opacity: .5;
                font-size: 0.75rem;
                letter-spacing: 0.08em;
            }

            /* Smooth scrolling and header offset */
            html {
                scroll-behavior: smooth;
            }

            /* Offset for fixed header navigation */
            #projects, #story, #contact {
                scroll-margin-top: 5rem;
            }

            #top {
                scroll-margin-top: 0;
            }

            /* Contact Form Styles - Expandable & Minimal */
            .contact-section {
                margin: 4.5rem auto;
            }

            .contact-header {
                cursor: pointer;
                transition: all 0.3s ease;
                border-bottom: 1px solid transparent;
                padding-bottom: var(--spacing-xs);
            }

            .contact-header:hover {
                border-bottom-color: var(--color-fg-main);
                opacity: 0.8;
            }

            .contact-header h2 {
                font-weight: 400;
                font-size: 1rem;
                text-transform: uppercase;
                margin: var(--spacing-md) 0 var(--spacing-xs) 0;
                display: inline-block;
            }

            .contact-form {
                max-width: 400px;
                margin: 0;
                max-height: 0;
                overflow: hidden;
                transition: max-height 0.4s ease, opacity 0.3s ease;
                opacity: 0;
            }

            .contact-form.expanded {
                max-height: 500px;
                opacity: 1;
                margin-top: var(--spacing-lg);
            }

            .form-group {
                margin-bottom: var(--spacing-md);
            }

            .form-group label {
                display: block;
                font-size: 0.75rem;
                text-transform: uppercase;
                margin-bottom: var(--spacing-xs);
                opacity: 0.6;
                letter-spacing: 0.05em;
            }

            .form-group input,
            .form-group textarea {
                width: 100%;
                padding: var(--spacing-xs) 0;
                border: none;
                border-bottom: 1px solid var(--color-fg-main);
                background: transparent;
                color: var(--color-fg-main);
                font-family: inherit;
                font-size: 0.875rem;
                resize: vertical;
                opacity: 0.8;
            }

            .form-group input:focus,
            .form-group textarea:focus {
                outline: none;
                border-bottom-color: var(--color-fg-main);
                opacity: 1;
            }

            .form-group textarea {
                min-height: 4rem;
                line-height: 1.4;
                border-bottom: 1px solid var(--color-fg-main);
            }

            .contact-submit {
                background: transparent;
                color: var(--color-fg-main);
                border: 1px solid var(--color-fg-main);
                padding: var(--spacing-xs) var(--spacing-md);
                font-family: inherit;
                font-size: 0.75rem;
                text-transform: uppercase;
                cursor: pointer;
                transition: all 0.3s ease;
                margin-top: var(--spacing-md);
                letter-spacing: 0.05em;
            }

            .contact-submit:hover {
                background: var(--color-fg-main);
                color: var(--color-bg-main);
            }

            .contact-submit:disabled {
                opacity: 0.5;
                cursor: not-allowed;
            }

            .contact-info {
                margin-bottom: var(--spacing-lg);
                opacity: 0.6;
                font-size: 0.875rem;
                transition: opacity 0.3s ease;
            }

            .contact-info.expanded {
                opacity: 0;
                margin-bottom: 0;
            }

            /* Resume specific styles */
            .resume-details {
                list-style: none;
                padding: 0;
                margin: 0;
                font-size: 0.875rem;
                line-height: 1.4;
                opacity: 0.8;
            }

            .resume-details li {
                margin-bottom: var(--spacing-sm);
                padding-left: var(--spacing-sm);
                position: relative;
            }

            .resume-details li::before {
                content: '•';
                position: absolute;
                left: 0;
                opacity: 0.5;
            }

            .skills-grid {
                display: grid;
                grid-template-columns: 1fr;
                gap: var(--spacing-lg);
                margin-top: var(--spacing-xl);
            }

            .skill-category h3 {
                font-size: 0.875rem;
                font-weight: 400;
                text-transform: uppercase;
                margin-bottom: var(--spacing-sm);
                opacity: 0.9;
            }

            .skill-category p {
                font-size: 0.875rem;
                line-height: 1.4;
                opacity: 0.7;
                margin: 0;
            }

            /* EXACT Long Nguyen Mobile Responsive */
            @media screen and (max-device-width: 480px) {
                body {
                    -webkit-text-size-adjust: 100%;
                }
            }

            @media screen and (min-width: 768px) {
                .vertical {
                    --spacing-vertical: var(--spacing-lg);
                }

                .horizontal {
                    --spacing-horizontal: 6rem;
                }

                header {
                    order: 0;
                    bottom: unset;
                    top: 0;
                }

                .intro-container {
                    grid-template-columns: 1fr;
                    row-gap: var(--spacing-md);
                }
                
                .intro-right {
                    text-align: left;
                }

                .intro-container .wrapper {
                    margin-top: 8rem;
                    margin-bottom: 10rem;
                }

                .works-grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    column-gap: var(--spacing-xl);
                }

                .project-card {
                    max-width: 512px;
                }

                .statement-section {
                    margin-top: 8.5rem;
                }

                .statement-container {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    grid-template-rows: auto;
                    column-gap: var(--spacing-xxl);
                }

                .statement-sub p {
                    margin-top: 0;
                }

                .statement-highlight {
                    grid-area: 1 / 1 / 2 / 2;
                }

                .statement-sub {
                    grid-area: 1 / 2 / 2 / 3;
                    margin-bottom: var(--spacing-xxl);
                }

                .footer-links {
                    display: grid;
                    grid-template-columns: 1fr 1fr 1fr;
                    column-gap: var(--spacing-lg);
                }

                .footer-links {
                    grid-template-columns: 1fr 1fr 1fr;
                    gap: var(--spacing-sm);
                }
                
                .footer-links li {
                    font-size: 1rem;
                }

                /* Timeline responsive - removed timeline visual elements */

                /* Skills grid responsive */
                .skills-grid {
                    grid-template-columns: 1fr 1fr;
                }
            }
        </style>
    </head>
    <body>
        <div id="top" class="container margin vertical flex flex-columns flex-nowrap">
            <!-- Header - EXACT Long Nguyen structure -->
            <header>
                <div class="container padding horizontal">
                    <div class="block">
                        <nav>
                            <div class="container-actions">
                                <h2><a href="#top">Michael Xie</a></h2>
                                <div class="links-container">
                                    <ul class="links-list">
                                        <li><a href="#top">Bio</a></li>
                                        <li><a href="#projects">Projects</a></li>
                                        <li><a href="#story">Story</a></li>
                                        <li><a href="#contact">Contact</a></li>
                                    </ul>
                                </div>
                            </div>
                        </nav>
                    </div>
                </div>
            </header>

            <!-- Main Content Container -->
            <div class="container margin horizontal flex flex-columns flex-grow">
                <main class="flex-grow">
                    <div class="block">
                        <!-- Intro Section - EXACT structure -->
                        <div class="block">
                            <div class="intro-container">
                                <div class="intro-left">
                                    <p>Senior Software Engineer based in Chicago, IL with extensive experience delivering scalable, enterprise-grade systems for leading financial institutions.</p>
                                </div>
                                <div class="intro-right">
                                    <ul>
                                        <li><a href="/resume">Resume</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <!-- Selected Works Section - EXACT structure -->
                        <section id="projects" class="block works-section">
                            <div class="wrapper">
                                <h2>Selected <br> Works ↘</h2>
                                <div class="works-grid">
                                    <div class="project-card" onclick="openModal('homelab')">
                                        <h3>HomeLab & Smart-Condo Automation <br><span class="fade">Infrastructure & DevOps</span></h3>
                                        <img src="/static/images/projects/homelab_image.png" alt="HomeLab & Smart-Condo Automation Platform" class="project-image">
                                        <p>Containerized environment powering home automation, analytics, and AI.</p>
                                    </div>

                                    <div class="project-card" onclick="openModal('real-estate')">
                                        <h3>Chicago Rental Analytics <br><span class="fade">Data Engineering & Visualization</span></h3>
                                        <img src="/static/images/projects/chicago_analytics_map.png" alt="Chicago Rental Analytics Dashboard" class="project-image">
                                        <p>Automated platform processing 75k+ records with ML insights.</p>
                                    </div>

                                    <div class="project-card" onclick="openModal('ai-ml')">
                                        <h3>AI/ML Playground <br><span class="fade">Artificial Intelligence</span></h3>
                                        <img src="/static/images/projects/aigeneratedai.png" alt="AI/ML Playground" class="project-image">
                                        <p>Self-hosted infrastructure with Stable Diffusion and LLM models.</p>
                                    </div>

                                    <div class="project-card" onclick="openModal('smart-home')">
                                        <h3>Smart-Home & IoT Ecosystem <br><span class="fade">IoT & Home Automation</span></h3>
                                        <img src="/static/images/projects/homeassistant.png" alt="Smart-Home & IoT Ecosystem" class="project-image">
                                        <p>DIY solutions with ESP32 boards and sensors for efficiency.</p>
                                    </div>
                                </div>
                                
                                <!-- See All Projects Link -->
                                <div class="see-all-container">
                                    <a href="/projects" class="see-all-link">see all projects ↘</a>
                                </div>
                            </div>
                        </section>

                        <!-- Developer Story Section - Inspired by Thea -->
                        <section id="story" class="block developer-story-section">
                            <div class="wrapper">
                                <h2>Developer <br> Story ↘</h2>
                                <div class="timeline-wrapper">
                                    <div class="timeline-item">
                                        <div class="timeline-content">
                                            <img src="/static/images/companies/uw_small.png" alt="University of Wisconsin-Madison" class="company-logo-large">
                                            <div class="timeline-text-content">
                                                <div class="timeline-type education">education</div>
                                                <div class="timeline-date">Aug 2014 - May 2018</div>
                                                <h3 class="education">University of Wisconsin-Madison</h3>
                                                <div class="timeline-company">Statistics & Computer Science</div>
                                                <p>Bachelor's degree focused on financial statistics, econometrics, and computational methods for large-scale data analysis.</p>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="timeline-item">
                                        <div class="timeline-content">
                                            <img src="/static/images/companies/northwestern_mutual_small.png" alt="Northwestern Mutual" class="company-logo-large">
                                            <div class="timeline-text-content">
                                                <div class="timeline-type work">work</div>
                                                <div class="timeline-date">Jun 2018 - Aug 2019</div>
                                                <h3 class="northwestern-mutual">Operations Lead</h3>
                                                <div class="timeline-company">Northwestern Mutual • Milwaukee, WI</div>
                                                <p>Managed enterprise iOS/Android app deployment using Microsoft Intune and Azure AD.</p>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="timeline-item">
                                        <div class="timeline-content">
                                            <img src="/static/images/companies/capital_one_small.png" alt="Capital One" class="company-logo-large">
                                            <div class="timeline-text-content">
                                                <div class="timeline-type work">work</div>
                                                <div class="timeline-date">Aug 2019 - Nov 2023</div>
                                                <h3 class="capital-one">Software Engineer</h3>
                                                <div class="timeline-company">Capital One • Chicago, IL</div>
                                                <p>Built scalable AWS ETL pipelines with Python/PySpark and fraud analytics systems using Java Spring Boot.</p>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="timeline-item">
                                        <div class="timeline-content">
                                            <img src="/static/images/companies/northern_trust_small.png" alt="Northern Trust" class="company-logo-large">
                                            <div class="timeline-text-content">
                                                <div class="timeline-type work">work</div>
                                                <div class="timeline-date">Mar 2025 - <strong>Present</strong></div>
                                                <h3 class="northern-trust">Software Engineer (IAM)</h3>
                                                <div class="timeline-company">Northern Trust • Chicago, IL</div>
                                                <p>Developing Python ETL pipelines for enterprise identity systems and automating legacy IAM data migration.</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <!-- Statement Section - Long Nguyen approach -->
                        <section class="block statement-section">
                            <div class="statement-container">
                                <p class="statement-highlight text-lg">
                                    Software Engineering. Data Engineering. API Development. Embedded Systems. Cloud & Infrastructure. Security & DevOps.
                                </p>
                                <div class="statement-sub">
                                    <p>
                                        6+ years specializing in Python, Java, ETL pipelines, AWS cloud infrastructure, 
                                        on-premises systems, and enterprise-scale data platforms at Fortune 500 companies.
                                    </p>
                                    <div>
                                        <a href="#story">My Journey ↘</a>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <!-- Contact Section -->
                        <section id="contact" class="block contact-section">
                            <div class="wrapper">
                                <div class="contact-header" onclick="toggleContactForm()">
                                    <h2>Contact ↘</h2>
                                </div>
                                <div class="contact-info">
                                    <p>Available for new opportunities and projects</p>
                                </div>
                                <form class="contact-form" action="mailto:xie.michael@icloud.com" method="post" enctype="text/plain">
                                    <div class="form-group">
                                        <label for="name">Name</label>
                                        <input type="text" id="name" name="name" required>
                                    </div>
                                    <div class="form-group">
                                        <label for="email">Email</label>
                                        <input type="email" id="email" name="email" required>
                                    </div>
                                    <div class="form-group">
                                        <label for="message">Message</label>
                                        <textarea id="message" name="message" placeholder="Your message..." required></textarea>
                                    </div>
                                    <button type="submit" class="contact-submit">Send</button>
                                </form>
                            </div>
                        </section>
                    </div>
                </main>

                <!-- Footer - EXACT Long Nguyen structure -->
                <footer class="block">
                    <div class="container">
                        <section class="footer-links">
                            <div>
                                <h2>Links ↘</h2>
                                <ul>
                                    <li><a href="#top">Bio</a></li>
                                    <li><a href="/projects" onclick="handleProjectsLink(event)">Projects</a></li>
                                    <li><a href="/resume" onclick="handleResumeLink(event)">Resume</a></li>
                                </ul>
                            </div>
                            <div>
                                <h2>Connect ↘</h2>
                                <ul>
                                    <li><a href="mailto:xie.michael@icloud.com">Email</a></li>
                                    <li><a href="#contact" onclick="expandContactForm()">Contact Form</a></li>
                                </ul>
                            </div>
                            <div>
                                <h2>Socials ↘</h2>
                                <ul>
                                    <li><a href="https://github.com/xie-git">Github</a></li>
                                    <li><a href="https://linkedin.com/in/xie-michael">LinkedIn</a></li>
                                </ul>
                            </div>
                        </section>
                                                     <small>© 2025 Michael Xie. All rights reserved.</small>
                    </div>
                </footer>
            </div>
        </div>

        <!-- Project Modal -->
        <div id="projectModal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeModal()">&times;</span>
                
                <!-- Left side: Image and title -->
                <div class="modal-left">
                    <div class="modal-header">
                        <h2 id="modalTitle" class="modal-title"></h2>
                        <div id="modalType" class="modal-type"></div>
                    </div>
                    <div id="modalImage" class="modal-image"></div>
                    <p id="modalOverview" class="modal-overview"></p>
                </div>
                
                <!-- Right side: Details -->
                <div class="modal-right">
                    <div class="modal-section">
                        <h3>Tech Stack</h3>
                        <div id="modalTechStack" class="tech-list"></div>
                    </div>
                    
                    <div class="modal-section">
                        <h3>Features</h3>
                        <ul id="modalFeatures" class="feature-list"></ul>
                    </div>
                    
                    <div class="modal-section">
                        <h3>Challenge</h3>
                        <p id="modalChallenges"></p>
                    </div>
                    
                    <div class="modal-section">
                        <h3>Impact</h3>
                        <p id="modalImpact"></p>
                    </div>
                </div>
            </div>
        </div>

        <script>
            // Project data for modal
            const projects = {
                'homelab': {
                    title: 'HomeLab & Smart-Condo Automation Platform',
                    type: 'Infrastructure & DevOps',
                    image: '/static/images/projects/homelab_image.png',
                    overview: 'Built a fully containerized, self-hosted environment that powers home automation, real-time analytics, media streaming, and on-device AI while serving as a playground for DevOps experimentation.',
                    tech_stack: ['Docker Compose', 'Ubuntu 24.04 LTS', 'Proxmox', 'Tailscale VPN', 'Home Assistant', 'InfluxDB', 'Grafana', 'Prometheus', 'Ollama LLM', 'Nextcloud', 'Plex'],
                    features: [
                        'Real-time environmental dashboard with sub-5s refresh',
                        'Self-hosted cloud suite replacing iCloud/Google Drive',
                        'Housing-market microservice with ML price-anomaly alerts',
                        'Media & gaming hub streaming 4K HDR video',
                        'Automated resilience with health-checks and failover'
                    ],
                    challenges: 'Unified heterogeneous hardware under single monitoring plane, tuned InfluxDB retention for 500ms refresh without data loss, hardened remote access eliminating exposed public ports.',
                    impact: '99.9% service uptime over 12 months, reduced cloud-storage spend by $240/yr, improved HVAC efficiency by 8%, delivered reusable DevOps sandbox cutting work project iteration time by 40%.'
                },
                'real-estate': {
                    title: 'Chicago Rental Analytics & Visualization Pipeline',
                    type: 'Data Engineering & Visualization',
                    image: '/static/images/projects/chicago_analytics_map.png',
                    overview: 'Designed, built, and production-hardened a fully automated data platform that scrapes, cleans, enriches, and visualizes 75k+ Chicago apartment records, delivering investment-grade insights via ML models and Grafana dashboards.',
                    tech_stack: ['Python 3.11', 'Docker Compose', 'PostgreSQL 14', 'Redis', 'scikit-learn', 'FastAPI', 'Folium', 'InfluxDB', 'Grafana', 'BeautifulSoup4'],
                    features: [
                        'Automated weekly pipeline processing 4,500 URLs in ~6h',
                        'Random-Forest price prediction model (R² = 0.995, RMSE ≈ $50)',
                        'Building-level insights with investment scores and risk metrics',
                        'Interactive Folium-powered clustering map with live queries',
                        'Six Grafana dashboards with sub-5s refresh',
                        'One-command DevOps deployment with 100% E2E test coverage'
                    ],
                    challenges: 'Implemented Redis task queue for 5 parallel scrapers cutting collection time 40%, built ID-fuzzing logic achieving 85%+ data quality, added model drift detection with automated retraining.',
                    impact: '75k+ property rows processed, 600 building insights generated, >99% weekly pipeline success rate over 6 months, enables neighborhood price comps and yield forecasts for investors.'
                },
                'ai-ml': {
                    title: 'AI/ML Playground',
                    type: 'Artificial Intelligence',
                    image: '/static/images/projects/aigeneratedai.png',
                    overview: 'A local AI development environment for experimenting with cutting-edge machine learning models while maintaining privacy and control.',
                    tech_stack: ['Stable Diffusion', 'Ollama', 'Python', 'PyTorch', 'CUDA', 'FastAPI', 'Docker'],
                    features: [
                        'Local Stable Diffusion image generation',
                        'Multiple LLM model hosting with Ollama',
                        'Custom model fine-tuning pipeline',
                        'API endpoints for integration',
                        'Prompt engineering tools',
                        'Model performance monitoring'
                    ],
                    challenges: 'Optimizing model performance on consumer hardware, managing GPU memory efficiently, and creating intuitive interfaces.',
                    impact: 'Accelerated AI/ML learning and provided a foundation for integrating AI into other projects.'
                },
                'smart-home': {
                    title: 'Smart-Home & IoT Ecosystem',
                    type: 'IoT & Home Automation',
                    image: '/static/images/projects/homeassistant.png',
                    overview: 'Architected and maintain a tightly-integrated suite of DIY smart-home solutions built on open-source software and low-cost microcontrollers to drive comfort, security, and data-driven energy efficiency across 1,250 sq ft condo.',
                    tech_stack: ['10× ESP32-WROOM-32', 'BME688 sensors', 'LD2450 mm-wave radars', 'ESPHome 2023.12', 'Home Assistant', 'Mosquitto MQTT', 'InfluxDB 2', 'Grafana', 'Tailscale VPN', 'Pi-hole DNS'],
                    features: [
                        'Sensor mesh coverage across 6 zones with real-time heat-maps',
                        'Adaptive HVAC & blinds balancing IAQ and comfort automatically',
                        'Presence-aware lighting with <100ms response via LD2450 radar',
                        'Energy & network dashboards with Slack anomaly alerting',
                        'Voice-first control via Mycroft AI (completely offline)',
                        'Whole-home ad-blocking via Pi-hole reducing WAN data 25%'
                    ],
                    challenges: 'Achieved low-latency telemetry without Wi-Fi saturation via tuned ESP32 QoS, calibrated sensor accuracy in mixed HVAC airflow, secured remote access migrating from port-forwards to Tailscale mesh.',
                    impact: 'Maintained temp ±1°C and humidity 40-55% year-round, achieved 99.9% service uptime, collected 2M+ time-series points, cut annual energy use 8%, provided DevOps sandbox shortening POC cycles 40%.'
                }
            };

            function openModal(projectId) {
                const project = projects[projectId];
                if (!project) return;

                // Populate modal content
                document.getElementById('modalTitle').textContent = project.title;
                document.getElementById('modalType').textContent = project.type;
                
                // Set modal image
                const modalImage = document.getElementById('modalImage');
                modalImage.innerHTML = `<img src="${project.image}" alt="${project.title}" style="width: 100%; height: 100%; object-fit: cover; opacity: 1;">`;
                
                document.getElementById('modalOverview').textContent = project.overview;
                document.getElementById('modalChallenges').textContent = project.challenges;
                document.getElementById('modalImpact').textContent = project.impact;

                // Tech stack
                const techStackContainer = document.getElementById('modalTechStack');
                techStackContainer.innerHTML = '';
                project.tech_stack.forEach(tech => {
                    const tag = document.createElement('span');
                    tag.className = 'tech-tag';
                    tag.textContent = tech;
                    techStackContainer.appendChild(tag);
                });

                // Features
                const featuresContainer = document.getElementById('modalFeatures');
                featuresContainer.innerHTML = '';
                project.features.forEach(feature => {
                    const li = document.createElement('li');
                    li.textContent = feature;
                    featuresContainer.appendChild(li);
                });

                // Show modal
                const modal = document.getElementById('projectModal');
                modal.classList.add('show');
                document.body.style.overflow = 'hidden';
            }

            function closeModal() {
                const modal = document.getElementById('projectModal');
                modal.classList.remove('show');
                document.body.style.overflow = 'auto';
            }

            // Close modal when clicking outside
            window.onclick = function(event) {
                const modal = document.getElementById('projectModal');
                if (event.target === modal) {
                    closeModal();
                }
            }

            // Make sure modal closes properly
            document.addEventListener('DOMContentLoaded', function() {
                const modal = document.getElementById('projectModal');
                if (modal) {
                    modal.classList.remove('show');
                }
            });

            // Close modal with Escape key
            document.addEventListener('keydown', function(event) {
                if (event.key === 'Escape') {
                    closeModal();
                }
            });

            // Contact form handler
            document.addEventListener('DOMContentLoaded', function() {
                const contactForm = document.querySelector('.contact-form');
                if (contactForm) {
                    contactForm.addEventListener('submit', function(e) {
                        e.preventDefault();
                        
                        const name = document.getElementById('name').value;
                        const email = document.getElementById('email').value;
                        const message = document.getElementById('message').value;
                        
                        const subject = `Portfolio Contact from ${name}`;
                        const mailtoLink = `mailto:xie.michael@icloud.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`)}`;
                        
                        window.location.href = mailtoLink;
                    });
                }
            });

            // Toggle contact form
            function toggleContactForm() {
                const header = document.querySelector('.contact-header');
                const form = document.querySelector('.contact-form');
                const info = document.querySelector('.contact-info');
                
                header.classList.toggle('expanded');
                form.classList.toggle('expanded');
                info.classList.toggle('expanded');
            }

            // Expand contact form (used when clicking "Contact Form" link)
            function expandContactForm() {
                const header = document.querySelector('.contact-header');
                const form = document.querySelector('.contact-form');
                const info = document.querySelector('.contact-info');
                
                // Add expanded class if not already expanded
                if (!form.classList.contains('expanded')) {
                    header.classList.add('expanded');
                    form.classList.add('expanded');
                    info.classList.add('expanded');
                }
            }
            
            // Handle footer link behaviors
            function handleProjectsLink(event) {
                if (window.location.pathname === '/projects') {
                    event.preventDefault();
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            }
            
            function handleResumeLink(event) {
                if (window.location.pathname === '/resume') {
                    event.preventDefault();
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            }
        </script>
    </body>
    </html>
    """
    
    @app.route('/')
    def home():
        return render_template_string(home_template)
    
    @app.route('/Xie_Data_Resume.pdf')
    def resume():
        return send_file('Xie_Data_Resume.pdf', as_attachment=False)
    
    @app.route('/projects')
    def all_projects():
        # Projects page template with extended grid
        projects_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                         <title>All Projects - Michael Xie</title>
            <style>
                /* Include all the same styles as main page */
                """ + home_template.split('<style>')[1].split('</style>')[0] + """
                
                /* Projects page specific styles */
                .projects-page {
                    min-height: 100vh;
                }
                
                .projects-page main {
                    margin-bottom: calc(var(--spacing-xxl) + 2rem);
                }
                
                .projects-header {
                    margin: var(--spacing-xxl) 0;
                }
                
                .projects-header h1 {
                    font-size: 1.5rem;
                    margin-bottom: var(--spacing-md);
                    text-transform: uppercase;
                }
                
                .back-link {
                    display: inline-block;
                    margin-bottom: var(--spacing-lg);
                    color: var(--color-fg-main);
                    text-decoration: none;
                    font-size: 0.875rem;
                    opacity: 0.6;
                    transition: opacity 0.3s ease;
                }
                
                .back-link:hover {
                    opacity: 1;
                    text-decoration: underline;
                }
                
                .extended-grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    column-gap: var(--spacing-xl);
                    row-gap: var(--spacing-xxl);
                }
                
                @media (max-width: 767px) {
                    .extended-grid {
                        grid-template-columns: 1fr;
                        gap: var(--spacing-xl);
                    }
                }
            </style>
        </head>
        <body>
            <div class="container margin vertical flex flex-columns flex-nowrap projects-page">
                <!-- Header - Same as main page -->
                <header>
                    <div class="container padding horizontal">
                        <div class="block">
                            <nav>
                                <div class="container-actions">
                                    <h2><a href="/">Michael Xie</a></h2>
                                    <div class="links-container">
                                        <ul class="links-list">
                                            <li><a href="/#top">About</a></li>
                                            <li><a href="/#contact" onclick="expandContactOnMainPage()">Contact</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </nav>
                        </div>
                    </div>
                </header>

                <!-- Main Content -->
                <div class="container margin horizontal flex flex-columns flex-grow">
                    <main class="flex-grow">
                                                 <div class="block">
                             <div class="projects-header">
                                 <a href="/" class="back-link">← back to home</a>
                                 <h1>All Projects</h1>
                                 <p style="opacity: 0.7; font-size: 0.875rem;">Technical projects and experiments.</p>
                             </div>
                            
                            <div class="extended-grid">
                                <div class="project-card" onclick="openModal('homelab')">
                                    <h3>HomeLab & Smart-Condo Automation <br><span class="fade">Infrastructure & DevOps</span></h3>
                                    <img src="/static/images/projects/homelab_image.png" alt="HomeLab & Smart-Condo Automation Platform" class="project-image">
                                    <p>Containerized environment powering home automation, analytics, and AI.</p>
                                </div>

                                <div class="project-card" onclick="openModal('real-estate')">
                                    <h3>Chicago Rental Analytics <br><span class="fade">Data Engineering & Visualization</span></h3>
                                    <img src="/static/images/projects/chicago_analytics_map.png" alt="Chicago Rental Analytics Dashboard" class="project-image">
                                    <p>Automated platform processing 75k+ records with ML insights.</p>
                                </div>

                                <div class="project-card" onclick="openModal('ai-ml')">
                                    <h3>AI/ML Playground <br><span class="fade">Artificial Intelligence</span></h3>
                                    <img src="/static/images/projects/aigeneratedai.png" alt="AI/ML Playground" class="project-image">
                                    <p>Self-hosted infrastructure with Stable Diffusion and LLM models.</p>
                                </div>

                                <div class="project-card" onclick="openModal('smart-home')">
                                    <h3>Smart-Home & IoT Ecosystem <br><span class="fade">IoT & Home Automation</span></h3>
                                    <img src="/static/images/projects/homeassistant.png" alt="Smart-Home & IoT Ecosystem" class="project-image">
                                    <p>Comprehensive sensor network with BME688, LD2450, and custom IoT devices integrated with Home Assistant automation.</p>
                                </div>
                                
                                <!-- Placeholder for future projects -->
                                <div class="project-card" style="opacity: 0.5; cursor: default;">
                                    <h3>Coming Soon • <br><span class="fade">Future Project</span></h3>
                                    <div class="project-placeholder">🔮</div>
                                    <p>More exciting projects are in development. Stay tuned for updates!</p>
                                </div>
                                
                                <div class="project-card" style="opacity: 0.5; cursor: default;">
                                    <h3>Coming Soon • <br><span class="fade">Future Project</span></h3>
                                    <div class="project-placeholder">⚡</div>
                                    <p>Additional technical experiments and innovations coming soon.</p>
                                </div>
                            </div>
                        </div>
                    </main>

                    <!-- Footer - Same as main page -->
                    <footer class="block">
                        <div class="container">
                            <section class="footer-links">
                                <div>
                                    <h2>Links ↘</h2>
                                    <ul>
                                        <li><a href="/#top">Bio</a></li>
                                        <li><a href="/projects" onclick="handleProjectsLink(event)">Projects</a></li>
                                        <li><a href="/resume" onclick="handleResumeLink(event)">Resume</a></li>
                                    </ul>
                                </div>
                                <div>
                                    <h2>Connect ↘</h2>
                                    <ul>
                                        <li><a href="mailto:xie.michael@icloud.com">Email</a></li>
                                        <li><a href="/#contact" onclick="expandContactOnMainPage()">Contact Form</a></li>
                                    </ul>
                                </div>
                                <div>
                                    <h2>Socials ↘</h2>
                                    <ul>
                                        <li><a href="https://github.com/xie-git">Github</a></li>
                                        <li><a href="https://linkedin.com/in/xie-michael">LinkedIn</a></li>
                                    </ul>
                                </div>
                            </section>
                            <small>© 2025 Michael Xie. All rights reserved.</small>
                        </div>
                    </footer>
                </div>
            </div>

            <!-- Same modal as main page -->
            """ + home_template.split('<!-- Project Modal -->')[1].split('</script>')[0] + """
            
            // Navigation behavior functions
            function expandContactOnMainPage() {
                if (window.location.pathname === '/') {
                    // On main page, expand contact form
                    expandContactForm();
                } else {
                    // On other pages, navigate to main page with contact expanded
                    window.location.href = '/#contact';
                    setTimeout(() => {
                        if (typeof expandContactForm === 'function') {
                            expandContactForm();
                        }
                    }, 100);
                }
            }
            
            // Handle footer link behaviors
            function handleProjectsLink(event) {
                if (window.location.pathname === '/projects') {
                    event.preventDefault();
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            }
            
            function handleResumeLink(event) {
                if (window.location.pathname === '/resume') {
                    event.preventDefault();
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            }
            </script>
        </body>
        </html>
        """
        return render_template_string(projects_template)

    @app.route('/resume')
    def resume_page():
        resume_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Resume - Michael Xie</title>
            <meta name="description" content="Michael Xie's detailed resume - Software Engineer specializing in data systems and enterprise infrastructure.">
            <style>
                """ + home_template.split('<style>')[1].split('</style>')[0] + """
            </style>
        </head>
        <body>
            <div id="top" class="container margin vertical flex flex-columns flex-nowrap resume-page">
                <!-- Header - EXACT Long Nguyen structure -->
                <header>
                    <div class="container padding horizontal">
                        <div class="block">
                            <nav>
                                <div class="container-actions">
                                    <h2><a href="/">Michael Xie</a></h2>
                                    <div class="links-container">
                                        <ul class="links-list">
                                            <li><a href="#experience">Experience</a></li>
                                            <li><a href="#education">Education</a></li>
                                            <li><a href="#projects">Projects</a></li>
                                            <li><a href="#skills">Skills</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </nav>
                        </div>
                    </div>
                </header>

                <!-- Main Content Container -->
                <div class="container margin horizontal flex flex-columns flex-grow">
                    <main class="flex-grow">
                        <div class="block">
                            <!-- Back Link -->
                            <div class="resume-header">
                                <a href="/" class="back-link">← back to home</a>
                            </div>
                            
                            <!-- Resume Header -->
                            <div class="block">
                                <div class="intro-container">
                                    <div class="intro-left">
                                        <p>Experienced Software Engineer specializing in scalable enterprise systems and AI-driven solutions. Expert in leveraging state-of-the-art AI models, tools, and techniques to accelerate enterprise development.</p>
                                    </div>
                                    <div class="intro-right">
                                    </div>
                                </div>
                            </div>

                            <!-- PDF Link -->
                            <div class="pdf-link-container">
                                <a href="/Xie_Data_Resume.pdf" target="_blank" class="pdf-download-link">Download PDF Resume ↘</a>
                            </div>

                            <!-- Experience Section -->
                            <section class="block" id="experience">
                                <div class="wrapper">
                                    <h2 onclick="toggleSection('experience-content')">Professional <br> Experience ↘</h2>
                                    <div id="experience-content" class="collapsible-content expanded">
                                        <ul class="resume-list">
                                        <li class="resume-list-item">
                                            <div class="resume-item-header">
                                                <h3 class="resume-item-title">Software Engineer (IAM)</h3>
                                                <p class="resume-item-company">Northern Trust • Chicago, IL</p>
                                                <p class="resume-item-date">Mar 2025 - Present</p>
                                            </div>
                                            <ul class="resume-item-details">
                                                <li>Developed and maintained Python-based ETL pipelines for enterprise identity systems using Linux and Control-M</li>
                                                <li>Automated and migrated legacy IAM data into modern platforms using secure OracleDB and PostgreSQL connections</li>
                                                <li>Provisioned on-prem infrastructure to support scheduled ETL workflows</li>
                                            </ul>
                                        </li>

                                        <li class="resume-list-item">
                                            <div class="resume-item-header">
                                                <h3 class="resume-item-title">Software Engineer</h3>
                                                <p class="resume-item-company">Capital One • Chicago, IL</p>
                                                <p class="resume-item-date">Aug 2019 - Nov 2023</p>
                                            </div>
                                            <ul class="resume-item-details">
                                                <li>Built scalable AWS Big Data ETL pipelines (Step Functions, EMR, DynamoDB, Lambda) using Python and PySpark to process sensitive customer credit and behavioral data for analytics and decisioning</li>
                                                <li>Created automated UI testing suite using Selenium and OpenCV for communication strategies deployed to delinquent customer segments</li>
                                                <li>Engineered a fraud analytics reporting system leveraging SQL, Snowflake, R, and Python, with dynamic dashboards enabling stakeholders to monitor the impact of evolving fraud logic</li>
                                                <li>Developed and maintained customer communication microservices using Java Spring Boot, containerized in Docker and deployed on ECS with CI/CD pipelines</li>
                                                <li>Standardized infrastructure pipelines for microservices, integrating Docker and AWS CI/CD tooling to streamline deployments</li>
                                            </ul>
                                        </li>

                                        <li class="resume-list-item">
                                            <div class="resume-item-header">
                                                <h3 class="resume-item-title">Operations Lead</h3>
                                                <p class="resume-item-company">Northwestern Mutual • Milwaukee, WI</p>
                                                <p class="resume-item-date">Jun 2018 - Aug 2019</p>
                                            </div>
                                            <ul class="resume-item-details">
                                                <li>Managed deployment of internal enterprise apps on iOS/Android using Microsoft Intune and Azure AD policies</li>
                                                <li>Resolved authentication and MDM compliance issues across employee devices and collaborated with internal support and security teams</li>
                                                <li>Coordinated between offshore development teams and on-site stakeholders; delivered weekly operations reports</li>
                                            </ul>
                                        </li>
                                        </ul>
                                    </div>
                                </div>
                            </section>

                            <!-- Education Section -->
                            <section class="block education-section" id="education">
                                <div class="wrapper">
                                    <h2 onclick="toggleSection('education-content')">Education ↘</h2>
                                    <div id="education-content" class="collapsible-content expanded">
                                        <ul class="resume-list">
                                        <li class="resume-list-item">
                                            <div class="resume-item-header">
                                                <h3 class="resume-item-title">University of Wisconsin-Madison</h3>
                                                <p class="resume-item-company">Statistics & Computer Science</p>
                                                <p class="resume-item-date">Aug 2014 - May 2018</p>
                                            </div>
                                            <ul class="resume-item-details">
                                                <li><strong>Degree:</strong> Bachelor of Science</li>
                                                <li><strong>Relevant Coursework:</strong> Data Structures & Algorithms, Database Systems, Financial Statistics, Statistical Programming, Mathematical Statistics, Linear Algebra</li>
                                            </ul>
                                        </li>
                                        </ul>
                                    </div>
                                </div>
                            </section>

                            <!-- Projects Section -->
                            <section class="block" id="projects">
                                <div class="wrapper">
                                    <h2 onclick="toggleSection('projects-content')">Key <br> Projects ↘</h2>
                                    <div id="projects-content" class="collapsible-content expanded">
                                        <ul class="resume-list">
                                        <li class="resume-list-item">
                                            <div class="resume-item-header">
                                                <h3 class="resume-item-title">HomeLab & Smart-Condo Automation Platform</h3>
                                                <p class="resume-item-company">Infrastructure & DevOps</p>
                                            </div>
                                            <ul class="resume-item-details">
                                                <li>Built fully containerized environment with Docker Compose managing 25+ containers (Home Assistant, Grafana, Prometheus, Ollama LLM)</li>
                                                <li>Achieved 99.9% service uptime, reduced cloud storage costs by $240/yr, improved HVAC efficiency by 8%</li>
                                                <li><strong>Tech Stack:</strong> Docker, Ubuntu, Proxmox, Tailscale VPN, InfluxDB, Grafana, Nextcloud, Plex</li>
                                            </ul>
                                        </li>

                                        <li class="resume-list-item">
                                            <div class="resume-item-header">
                                                <h3 class="resume-item-title">Chicago Rental Analytics & Visualization Pipeline</h3>
                                                <p class="resume-item-company">Data Engineering & ML</p>
                                            </div>
                                            <ul class="resume-item-details">
                                                <li>Automated data platform processing 75k+ Chicago apartment records with Random Forest ML model (R² = 0.995)</li>
                                                <li>Developed scalable data collection system with load-based scaling for comprehensive market analysis</li>
                                                <li>Created personal analytics platform for real estate insights and apartment hunting decisions, shared with friends for market intelligence</li>
                                                <li><strong>Tech Stack:</strong> Python, Docker, PostgreSQL, Redis, scikit-learn, FastAPI, Grafana</li>
                                            </ul>
                                        </li>

                                        <li class="resume-list-item">
                                            <div class="resume-item-header">
                                                <h3 class="resume-item-title">Smart-Home & IoT Ecosystem</h3>
                                                <p class="resume-item-company">IoT & Home Automation</p>
                                            </div>
                                            <ul class="resume-item-details">
                                                <li>Architected DIY smart-home with 10× ESP32 boards, BME688 sensors, LD2450 radar across 1,250 sq ft condo</li>
                                                <li>Maintained temp ±1°C, achieved 99.9% uptime, collected 2M+ time-series points, cut energy use 8%</li>
                                                <li><strong>Tech Stack:</strong> ESP32, ESPHome, Home Assistant, MQTT, InfluxDB, Grafana, Tailscale</li>
                                            </ul>
                                        </li>

                                        <li class="resume-list-item">
                                            <div class="resume-item-header">
                                                <h3 class="resume-item-title">AI/ML Playground</h3>
                                                <p class="resume-item-company">Artificial Intelligence</p>
                                            </div>
                                            <ul class="resume-item-details">
                                                <li>Self-hosted AI infrastructure with Stable Diffusion image generation and Ollama language models</li>
                                                <li>Created local development environment for experimenting with cutting-edge ML models while maintaining privacy</li>
                                                <li><strong>Tech Stack:</strong> Stable Diffusion, Ollama, Python, PyTorch, CUDA, FastAPI, Docker</li>
                                            </ul>
                                        </li>
                                        </ul>
                                    </div>
                                </div>
                            </section>

                            <!-- Certifications Section -->
                            <section class="block">
                                <div class="wrapper">
                                    <h2 onclick="toggleSection('certifications-content')">Certifications ↘</h2>
                                    <div id="certifications-content" class="collapsible-content expanded">
                                        <div class="certifications-content">
                                        <div class="certification-category">
                                            <h3>Technical Certifications</h3>
                                            <ul class="resume-item-details">
                                                <li>AWS Certified Solutions Architect - Associate</li>
                                            </ul>
                                        </div>
                                        
                                        <div class="certification-category">
                                            <h3>Professional Certifications</h3>
                                            <ul class="resume-item-details">
                                                <li>Coming Soon</li>
                                            </ul>
                                        </div>
                                        </div>
                                    </div>
                                </div>
                            </section>

                            <!-- Technical Skills Section -->
                            <section class="block" id="skills">
                                <div class="wrapper">
                                    <h2 onclick="toggleSection('skills-content')">Technical Skills ↘</h2>
                                    <div id="skills-content" class="collapsible-content expanded">
                                        <div class="skills-content">
                                        <div class="skill-category">
                                            <h3>Languages</h3>
                                            <p>Python, Java, SQL, R, JavaScript, Bash, YAML, Markdown</p>
                                        </div>
                                        
                                        <div class="skill-category">
                                            <h3>Cloud & Infrastructure</h3>
                                            <p>AWS (Lambda, ECS, EMR, Step Functions, DynamoDB, S3, SNS, SQS, RDS, CloudWatch, IAM), Docker, Kubernetes, Linux, Azure, Hypervisor, Control-M, Home Assistant, MQTT</p>
                                        </div>
                                        
                                        <div class="skill-category">
                                            <h3>Data & Analytics</h3>
                                            <p>PySpark, Snowflake, PostgreSQL, OracleDB, Databricks, Kafka, ETL, Pandas, Beautiful Soup, Selenium, Grafana, Prometheus, InfluxDB, Tableau</p>
                                        </div>
                                        
                                        <div class="skill-category">
                                            <h3>AI & Machine Learning</h3>
                                            <p>Self-Hosted Large Language Models (Ollama, Gemini, Claude, DeepSeek, GPT), AI Model Integration, Agentic Software Development, Model Evaluation & Optimization, Stable Diffusion, Image & LLM Model Fine-Tuning, OpenCV</p>
                                        </div>
                                        
                                        <div class="skill-category">
                                            <h3>Development</h3>
                                            <p>Spring Boot, RESTful APIs, Microservices Architecture, CI/CD (AWS CodePipeline, GitHub Actions), Testing Frameworks (JUnit, PyTest, Cucumber), Git, Maven, Embedded Systems (ESP32, ESP8266, BME688, LD2450), Web Scraping, Selenium Automation</p>
                                        </div>
                                        
                                        <div class="skill-category">
                                            <h3>Security & Compliance</h3>
                                            <p>PGP Encryption, Data Obfuscation, Sensitive Data Handling (NPI), Security Protocols (Finance & Banking Standards)</p>
                                        </div>
                                        
                                        <div class="skill-category">
                                            <h3>Networking</h3>
                                            <p>SMB, Basic Network Administration, Pi-hole, Home Networking, Wake-on-LAN</p>
                                        </div>
                                        
                                        <div class="skill-category">
                                            <h3>Project Management & Collaboration</h3>
                                            <p>Agile Methodology, Jira, Azure DevOps (ADO), Scrum, Kanban, Cross-functional Team Collaboration</p>
                                        </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                    </main>

                    <!-- Footer -->
                    <footer class="block">
                        <div class="container">
                            <section class="footer-links">
                                <div>
                                    <h2>Links ↘</h2>
                                    <ul>
                                        <li><a href="/#top">Bio</a></li>
                                        <li><a href="/projects" onclick="handleProjectsLink(event)">Projects</a></li>
                                        <li><a href="/resume" onclick="handleResumeLink(event)">Resume</a></li>
                                    </ul>
                                </div>
                                <div>
                                    <h2>Connect ↘</h2>
                                    <ul>
                                        <li><a href="mailto:xie.michael@icloud.com">Email</a></li>
                                        <li><a href="/#contact" onclick="expandContactOnMainPage()">Contact Form</a></li>
                                    </ul>
                                </div>
                                <div>
                                    <h2>Socials ↘</h2>
                                    <ul>
                                        <li><a href="https://github.com/xie-git">Github</a></li>
                                        <li><a href="https://linkedin.com/in/xie-michael">LinkedIn</a></li>
                                    </ul>
                                </div>
                            </section>
                            <small>© 2025 Michael Xie. All rights reserved.</small>
                        </div>
                    </footer>
                </div>
            </div>
            
            <script>
                function toggleSection(sectionId) {
                    const content = document.getElementById(sectionId);
                    if (content.classList.contains('expanded')) {
                        content.classList.remove('expanded');
                        content.classList.add('collapsed');
                    } else {
                        content.classList.remove('collapsed');
                        content.classList.add('expanded');
                    }
                }
                
                // Navigation behavior functions
                function expandContactOnMainPage() {
                    window.location.href = '/#contact';
                    setTimeout(() => {
                        if (typeof expandContactForm === 'function') {
                            expandContactForm();
                        }
                    }, 100);
                }
                
                // Handle footer link behaviors
                function handleProjectsLink(event) {
                    if (window.location.pathname === '/projects') {
                        event.preventDefault();
                        window.scrollTo({ top: 0, behavior: 'smooth' });
                    }
                }
                
                function handleResumeLink(event) {
                    if (window.location.pathname === '/resume') {
                        event.preventDefault();
                        window.scrollTo({ top: 0, behavior: 'smooth' });
                    }
                }
            </script>
        </body>
        </html>
        """
        return render_template_string(resume_template)

    return app

# This is the entry point for Gunicorn, which Render will use
app = create_app()
