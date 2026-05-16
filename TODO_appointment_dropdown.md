# TODO - Appointment booking dropdown (New / Revisit)

- [ ] Update `flask_projct/templates/appointment.html` to add a dropdown for appointment type (New / Revisit/Follow-up) and reveal an optional previous appointment reference field when Revisit is selected.
- [ ] Update `flask_projct/app.py`:
  - [ ] Add `appointments` table in `init_db()`.
  - [ ] Change `/appointment` route to accept POST.
  - [ ] On POST, insert appointment data into `appointments` table (previous appointment reference optional).
  - [ ] Flash success/error messages and redirect back to `/appointment`.
- [ ] Add flash message rendering to `appointment.html` (if not present).
- [ ] Manual test:
  - [ ] New appointment submits and records row.
  - [ ] Revisit appointment submits with/without previous reference and records row.

