# Rebold Zambia Job System: Design

## Purpose

Rebold Zambia Limited receives enquiries on Facebook that move to WhatsApp. Most services need a site visit before a quote, and follow-ups are easily forgotten. This system tracks every enquiry from first contact to payment, so no client is lost or forgotten.

## Users

- **Owner**: oversees all jobs, follow-ups, payments and revenue.
- **Staff**: log enquiries, schedule site visits, prepare and send quotes.
- **Technicians**: carry out site visits and jobs, and update their status.

## Two ways work comes in

**1. Services (site visit first):** camera installation, gate motor installation, repairs and maintenance, paving, building, painting.

**2. Goods supply (direct quote):** the customer enters specifications, staff check availability, and if available a quote is written and shared.

## User stories

- As **staff**, I want to log a WhatsApp enquiry in under a minute, so that no enquiry is lost.
- As **staff**, I want to schedule site visits and assign them to a technician.
- As a **technician**, I want to see my assigned visits and jobs and update their status from my phone.
- As **staff**, I want to write a quote from the technician's site visit report.
- As a **customer**, I want to submit my goods supply specifications and receive a quote if the goods are available.
- As the **owner**, I want a daily list of overdue follow-ups, so that no client is forgotten.
- As the **owner**, I want to see which jobs are unpaid and what each service line earns.

## Job lifecycle

```
Service:  Request received -> Visit scheduled -> Visit done -> Quote sent
Supply:   Request received -> Availability checked -> Quote sent (if available)

Quote sent -> Accepted -> Scheduled -> In progress -> Completed -> Paid
           -> Declined / No reply
```

Every job has a **next action** and a **due date**. Overdue next actions are flagged every morning. This is the core feature, because forgotten follow-ups are the main problem.

## Data model

| Table | Key columns |
|---|---|
| users | user_id, name, phone, role (owner / staff / technician) |
| clients | client_id, full_name, phone, location, source, created_at |
| services | service_id, name |
| products | product_id, name, brand, model, price, stock_quantity, is_available |
| jobs | job_id, client_id, job_type (service / supply), service_id, status, assigned_to, next_action, next_action_due, created_at |
| site_visits | visit_id, job_id, technician_id, scheduled_for, notes, completed |
| supply_requests | request_id, job_id, specifications, availability_status |
| quotes | quote_id, job_id, total, sent_at, valid_until, status |
| quote_items | item_id, quote_id, product_id (optional), description, quantity, unit_price |
| payments | payment_id, job_id, amount, method (cash / mobile money / bank), paid_at |
