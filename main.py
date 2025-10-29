import flet as ft
from datetime import datetime, timedelta

class LeaveRequestApp:
    def __init__(self):
        self.user_data = {}
        self.leave_requests = [
            {
                "name": "Liam Johnson",
                "type": "Vacation",
                "dates": "Mar 10 - Mar 15, 2024",
                "status": "Pending",
                "reason": "Family vacation"
            },
            {
                "name": "Olivia Chen",
                "type": "Sick Leave",
                "dates": "Mar 12, 2024",
                "status": "Approved",
                "reason": "Medical appointment"
            },
            {
                "name": "Noah Patel",
                "type": "Maternity",
                "dates": "Apr 01 - Jun 30, 2024",
                "status": "Rejected",
                "reason": "Maternity leave for childbirth"
            },
            {
                "name": "Emma Rodriguez",
                "type": "Annual Vacation",
                "dates": "Mar 20 - Mar 28, 2024",
                "status": "Approved",
                "reason": "Annual vacation with family"
            }
        ]

    def main(self, page: ft.Page):
        page.title = "HR Leave Request System"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.padding = 0
        
        # Store form data
        form_data = {}
        
        # Error message controls
        email_error = ft.Text(
            "Email is required",
            color="red400",
            size=12,
            visible=False
        )
        password_error = ft.Text(
            "Password is required",
            color="red400",
            size=12,
            visible=False
        )
        
        # Form field controls
        employee_name_field = ft.TextField(
            label="Employee Name",
            hint_text="Enter employee name",
            border_color="grey400",
        )
        
        department_dropdown = ft.Dropdown(
            label="Department",
            hint_text="Select department",
            options=[
                ft.dropdown.Option("Design Department"),
                ft.dropdown.Option("Engineering"),
                ft.dropdown.Option("Marketing"),
                ft.dropdown.Option("Human Resources"),
                ft.dropdown.Option("Finance"),
            ],
        )
        
        leave_type_dropdown = ft.Dropdown(
            label="Leave Type",
            hint_text="Select leave type",
            options=[
                ft.dropdown.Option("Vacation"),
                ft.dropdown.Option("Sick Leave"),
                ft.dropdown.Option("Maternity"),
                ft.dropdown.Option("Paternity"),
                ft.dropdown.Option("Annual Leave"),
            ],
        )
        
        start_date_button = ft.ElevatedButton(
            "Select start date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: pick_start_date(e)
        )
        
        end_date_button = ft.ElevatedButton(
            "Select end date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: pick_end_date(e)
        )
        
        reason_field = ft.TextField(
            label="Reason",
            hint_text="Please provide a reason",
            multiline=True,
            min_lines=3,
            max_lines=5,
        )
        
        # Date picker handlers
        def on_start_date_change(e):
            form_data["start_date"] = e.control.value
            start_date_button.text = e.control.value.strftime("%b %d, %Y")
            page.update()
        
        def on_end_date_change(e):
            form_data["end_date"] = e.control.value
            end_date_button.text = e.control.value.strftime("%b %d, %Y")
            page.update()
        
        # Create date pickers
        start_date_picker = ft.DatePicker(
            on_change=on_start_date_change,
            first_date=datetime.now(),
            last_date=datetime.now() + timedelta(days=365),
        )
        
        end_date_picker = ft.DatePicker(
            on_change=on_end_date_change,
            first_date=datetime.now(),
            last_date=datetime.now() + timedelta(days=365),
        )
        
        # Add date pickers to page overlay
        page.overlay.extend([start_date_picker, end_date_picker])
        
        def pick_start_date(e):
            start_date_picker.open = True
            page.update()
        
        def pick_end_date(e):
            end_date_picker.open = True
            page.update()
        
        # Navigation functions
        def go_to_home(e):
            page.go("/home")
        
        def go_to_form(e):
            page.go("/form")
        
        def go_to_details(e):
            # Validate form
            if not employee_name_field.value:
                employee_name_field.error_text = "This field is required"
                page.update()
                return
            
            # Store form data
            form_data["name"] = employee_name_field.value
            form_data["department"] = department_dropdown.value
            form_data["leave_type"] = leave_type_dropdown.value
            form_data["reason"] = reason_field.value
            
            page.go("/details")
        
        def go_to_history(e):
            page.go("/history")
        
        # Login function
        def handle_login(e):
            email_valid = bool(email_field.value)
            password_valid = bool(password_field.value)
            
            email_error.visible = not email_valid
            password_error.visible = not password_valid
            
            if email_valid and password_valid:
                page.go("/home")
            
            page.update()
        
        # Login page
        email_field = ft.TextField(
            label="Email",
            hint_text="Enter your email",
            prefix_icon=ft.Icons.EMAIL,
            width=300,
        )
        
        password_field = ft.TextField(
            label="Password",
            hint_text="Enter your password",
            prefix_icon=ft.Icons.LOCK,
            password=True,
            can_reveal_password=True,
            width=300,
        )
        
        login_view = ft.View(
            "/",
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=80, color="blue"),
                            ft.Text("HR Leave Request", size=32, weight=ft.FontWeight.BOLD),
                            ft.Text("Sign in to continue", size=16, color="grey700"),
                            ft.Container(height=30),
                            email_field,
                            email_error,
                            ft.Container(height=10),
                            password_field,
                            password_error,
                            ft.Container(height=30),
                            ft.ElevatedButton(
                                "Login",
                                width=300,
                                height=45,
                                on_click=handle_login,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    expand=True,
                    padding=20,
                )
            ],
        )
        
        # Home page
        home_view = ft.View(
            "/home",
            [
                ft.AppBar(
                    title=ft.Text("HR Leave Request Home"),
                    bgcolor="blue",
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Icon(ft.Icons.PERSON, size=40),
                                    ft.Text("Hello, HR Staff", size=20, weight=ft.FontWeight.BOLD),
                                    ft.IconButton(icon=ft.Icons.NOTIFICATIONS, icon_color="blue"),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Container(height=20),
                            ft.Row(
                                [
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Text("Pending Requests", size=14, color="grey700"),
                                                ft.Text("12", size=32, weight=ft.FontWeight.BOLD),
                                            ],
                                        ),
                                        bgcolor="blue50",
                                        padding=20,
                                        border_radius=10,
                                        expand=True,
                                    ),
                                    ft.Container(width=10),
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Text("Approved Today", size=14, color="grey700"),
                                                ft.Text("5", size=32, weight=ft.FontWeight.BOLD),
                                            ],
                                        ),
                                        bgcolor="green50",
                                        padding=20,
                                        border_radius=10,
                                        expand=True,
                                    ),
                                ],
                            ),
                            ft.Container(height=20),
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("Upcoming Leave", size=14, color="grey700"),
                                        ft.Text("3", size=32, weight=ft.FontWeight.BOLD),
                                    ],
                                ),
                                bgcolor="orange50",
                                padding=20,
                                border_radius=10,
                            ),
                            ft.Container(height=30),
                            ft.ElevatedButton(
                                "Request Leave",
                                width=300,
                                height=50,
                                on_click=go_to_form,
                                bgcolor="blue",
                                color="white",
                            ),
                            ft.Container(height=10),
                            ft.OutlinedButton(
                                "View Leave History",
                                width=300,
                                height=50,
                                on_click=go_to_history,
                            ),
                            ft.Container(height=30),
                            ft.Text("Quick Actions", size=18, weight=ft.FontWeight.BOLD),
                            ft.Container(height=10),
                            ft.Row(
                                [
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Icon(ft.Icons.ANNOUNCEMENT, size=30, color="blue"),
                                                ft.Text("Create\nAnnouncement", size=12, text_align=ft.TextAlign.CENTER),
                                                ft.Text("Notify all employees", size=10, color="grey600", text_align=ft.TextAlign.CENTER),
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        bgcolor="white",
                                        padding=15,
                                        border_radius=10,
                                        border=ft.border.all(1, "grey300"),
                                        expand=True,
                                    ),
                                    ft.Container(width=10),
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Icon(ft.Icons.CALENDAR_MONTH, size=30, color="blue"),
                                                ft.Text("View Team\nSchedule", size=12, text_align=ft.TextAlign.CENTER),
                                                ft.Text("Check weekly calendar", size=10, color="grey600", text_align=ft.TextAlign.CENTER),
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        bgcolor="white",
                                        padding=15,
                                        border_radius=10,
                                        border=ft.border.all(1, "grey300"),
                                        expand=True,
                                    ),
                                ],
                            ),
                        ],
                        scroll=ft.ScrollMode.AUTO,
                    ),
                    padding=20,
                    expand=True,
                )
            ],
        )
        
        # Form page
        form_view = ft.View(
            "/form",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_to_home),
                    title=ft.Text("New Leave Request"),
                    bgcolor="blue",
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            employee_name_field,
                            ft.Container(height=10),
                            department_dropdown,
                            ft.Container(height=10),
                            leave_type_dropdown,
                            ft.Container(height=20),
                            ft.Text("Start Date", size=14, weight=ft.FontWeight.BOLD),
                            start_date_button,
                            ft.Container(height=10),
                            ft.Text("End Date", size=14, weight=ft.FontWeight.BOLD),
                            end_date_button,
                            ft.Container(height=20),
                            reason_field,
                            ft.Container(height=30),
                            ft.ElevatedButton(
                                "Submit",
                                width=300,
                                height=50,
                                on_click=go_to_details,
                                bgcolor="blue",
                                color="white",
                            ),
                            ft.Container(height=10),
                            ft.OutlinedButton(
                                "Cancel",
                                width=300,
                                height=50,
                                on_click=go_to_home,
                            ),
                        ],
                        scroll=ft.ScrollMode.AUTO,
                    ),
                    padding=20,
                    expand=True,
                )
            ],
        )
        
        # Details page
        def create_details_view():
            start_date_str = form_data.get("start_date", datetime.now()).strftime("%b %d, %Y") if form_data.get("start_date") else "Not set"
            end_date_str = form_data.get("end_date", datetime.now()).strftime("%b %d, %Y") if form_data.get("end_date") else "Not set"
            
            # Calculate days
            days = 1
            if form_data.get("start_date") and form_data.get("end_date"):
                days = (form_data["end_date"] - form_data["start_date"]).days + 1
            
            def approve_request(e):
                # Show success snackbar
                page.snack_bar = ft.SnackBar(
                    content=ft.Text("Leave request approved successfully!"),
                    bgcolor="green",
                )
                page.snack_bar.open = True
                page.update()
                # Go to home after a short delay
                page.go("/home")
            
            def reject_request(e):
                # Show reject snackbar
                page.snack_bar = ft.SnackBar(
                    content=ft.Text("Leave request rejected"),
                    bgcolor="red",
                )
                page.snack_bar.open = True
                page.update()
                # Go to home after a short delay
                page.go("/home")
            
            return ft.View(
                "/details",
                [
                    ft.AppBar(
                        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_to_form),
                        title=ft.Text("Request Summary"),
                        bgcolor="blue",
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Container(
                                                content=ft.Text("Pending", color="orange900"),
                                                bgcolor="orange200",
                                                padding=ft.padding.symmetric(horizontal=15, vertical=5),
                                                border_radius=5,
                                            ),
                                            ft.Container(height=20),
                                            ft.Row(
                                                [
                                                    ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=60, color="grey"),
                                                    ft.Column(
                                                        [
                                                            ft.Text(form_data.get("name", "N/A"), size=20, weight=ft.FontWeight.BOLD),
                                                            ft.Text(form_data.get("department", "N/A"), color="grey700"),
                                                        ],
                                                        spacing=2,
                                                    ),
                                                ],
                                            ),
                                            ft.Divider(height=30),
                                            ft.Row(
                                                [
                                                    ft.Text("Leave Type", color="grey700", expand=True),
                                                    ft.Text(form_data.get("leave_type", "N/A"), weight=ft.FontWeight.BOLD),
                                                ],
                                            ),
                                            ft.Container(height=10),
                                            ft.Row(
                                                [
                                                    ft.Text("Start Date", color="grey700", expand=True),
                                                    ft.Text(start_date_str, weight=ft.FontWeight.BOLD),
                                                ],
                                            ),
                                            ft.Container(height=10),
                                            ft.Row(
                                                [
                                                    ft.Text("End Date", color="grey700", expand=True),
                                                    ft.Text(end_date_str, weight=ft.FontWeight.BOLD),
                                                ],
                                            ),
                                            ft.Container(height=10),
                                            ft.Row(
                                                [
                                                    ft.Text("Total", color="grey700", expand=True),
                                                    ft.Text(f"{days} Days", weight=ft.FontWeight.BOLD),
                                                ],
                                            ),
                                            ft.Divider(height=30),
                                            ft.Text("Reason", size=16, weight=ft.FontWeight.BOLD),
                                            ft.Container(height=5),
                                            ft.Text(
                                                form_data.get("reason", "No reason provided"),
                                                color="grey700",
                                            ),
                                        ],
                                    ),
                                    bgcolor="white",
                                    padding=20,
                                    border_radius=10,
                                    border=ft.border.all(1, "grey300"),
                                ),
                                ft.Container(height=30),
                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                            "Approve",
                                            expand=True,
                                            height=50,
                                            on_click=approve_request,
                                            bgcolor="green",
                                            color="white",
                                            icon=ft.Icons.CHECK_CIRCLE,
                                        ),
                                        ft.Container(width=10),
                                        ft.ElevatedButton(
                                            "Reject",
                                            expand=True,
                                            height=50,
                                            on_click=reject_request,
                                            bgcolor="red",
                                            color="white",
                                            icon=ft.Icons.CANCEL,
                                        ),
                                    ],
                                ),
                                ft.Container(height=10),
                                ft.OutlinedButton(
                                    "Back to Form",
                                    width=300,
                                    height=50,
                                    on_click=go_to_form,
                                ),
                            ],
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        padding=20,
                        expand=True,
                    )
                ],
            )
        
        # History page
        def create_history_view():
            leave_items = []
            
            for req in self.leave_requests:
                status_color = "orange200" if req["status"] == "Pending" else (
                    "green200" if req["status"] == "Approved" else "red200"
                )
                status_text_color = "orange900" if req["status"] == "Pending" else (
                    "green900" if req["status"] == "Approved" else "red900"
                )
                
                leave_items.append(
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=40, color="grey"),
                                ft.Column(
                                    [
                                        ft.Text(req["name"], size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text(f"{req['type']}: {req['dates']}", size=12, color="grey700"),
                                    ],
                                    spacing=2,
                                    expand=True,
                                ),
                                ft.Container(
                                    content=ft.Text(req["status"], size=12, color=status_text_color),
                                    bgcolor=status_color,
                                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                    border_radius=5,
                                ),
                                ft.IconButton(icon=ft.Icons.MORE_VERT),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        bgcolor="white",
                        padding=15,
                        border_radius=10,
                        border=ft.border.all(1, "grey300"),
                        margin=ft.margin.only(bottom=10),
                    )
                )
            
            return ft.View(
                "/history",
                [
                    ft.AppBar(
                        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_to_home),
                        title=ft.Text("Leave Requests"),
                        bgcolor="blue",
                        actions=[
                            ft.IconButton(icon=ft.Icons.MORE_VERT),
                        ],
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.TextField(
                                    hint_text="Search by employee name...",
                                    prefix_icon=ft.Icons.SEARCH,
                                    border_color="grey400",
                                ),
                                ft.Container(height=10),
                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                            "All",
                                            bgcolor="blue",
                                            color="white",
                                        ),
                                        ft.OutlinedButton("Pending"),
                                        ft.OutlinedButton("Approved"),
                                        ft.OutlinedButton("Rejected"),
                                    ],
                                    scroll=ft.ScrollMode.AUTO,
                                ),
                                ft.Container(height=20),
                                *leave_items,
                            ],
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        padding=20,
                        expand=True,
                    )
                ],
            )
        
        # Route change handler
        def route_change(route):
            page.views.clear()
            
            if page.route == "/":
                page.views.append(login_view)
            elif page.route == "/home":
                page.views.append(home_view)
            elif page.route == "/form":
                page.views.append(form_view)
            elif page.route == "/details":
                page.views.append(create_details_view())
            elif page.route == "/history":
                page.views.append(create_history_view())
            
            page.update()
        
        def view_pop(view):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
        
        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)


# Run the app
if __name__ == "__main__":
    app = LeaveRequestApp()
    ft.app(app.main, view=ft.WEB_BROWSER, port=8550)