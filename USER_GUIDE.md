# 📱 Absolute Stone Design App - User Guide

**Version:** 3.0.17  
**Last Updated:** January 2026  
**Design Approach:** Product Designer - User-Centered Documentation

---

## 🎯 Design Philosophy

This guide is designed with a **product designer mindset**, focusing on:
- **User Journeys**: Step-by-step flows that match how users actually interact with the app
- **Visual Hierarchy**: Scannable content with clear sections and visual breaks
- **Contextual Help**: Information provided when and where users need it
- **User Empathy**: Understanding user goals, not just features
- **Progressive Disclosure**: Showing information progressively as users need it
- **Error Prevention**: Guidance to help users avoid common mistakes

---

## 👥 User Personas

### 🏠 **Client (Sarah)**
- **Goal**: Find the perfect stone for her kitchen renovation
- **Pain Points**: Overwhelmed by choices, needs expert advice, wants to see materials before deciding
- **Tech Comfort**: Moderate - uses apps regularly but needs clear guidance
- **Primary Use**: Browse materials, chat with sales rep, create contract, track installation

### 💼 **Sales Rep (Mike)**
- **Goal**: Manage clients efficiently and close more sales
- **Pain Points**: Too many clients to track, needs quick access to project status
- **Tech Comfort**: High - comfortable with business apps
- **Primary Use**: Client management, chat inbox, project tracking, analytics

### 🔧 **Installer (Carlos)**
- **Goal**: Complete installations on time and keep clients happy
- **Pain Points**: Managing multiple jobs, updating status, sharing progress photos
- **Tech Comfort**: Moderate - prefers simple, straightforward interfaces
- **Primary Use**: View active jobs, update status, upload photos, manage availability

### 📅 **Scheduler (Jennifer)**
- **Goal**: Keep calendar organized and coordinate all appointments
- **Pain Points**: Multiple event types, syncing with Google Calendar, avoiding conflicts
- **Tech Comfort**: High - uses calendar apps daily
- **Primary Use**: Create events, manage calendar, coordinate appointments

### 👨‍💼 **Admin (David)**
- **Goal**: Oversee entire platform and ensure smooth operations
- **Pain Points**: Managing multiple user types, content updates, system monitoring
- **Tech Comfort**: Very High - technical background
- **Primary Use**: User management, content management, analytics, notifications

---

## 🗺️ User Journey Maps

### Client Journey: From Discovery to Installation

```
┌─────────────────────────────────────────────────────────────────┐
│                    CLIENT USER JOURNEY                           │
└─────────────────────────────────────────────────────────────────┘

1. DISCOVERY
   └─> Opens app (Web: immediate | Mobile: onboarding)
       └─> Browses materials as guest
           └─> Finds interesting material
               └─> Wants to chat with sales rep
                   └─> 🔐 Auth dialog appears
                       └─> Signs up

2. ENGAGEMENT
   └─> Chats with sales rep
       └─> Gets recommendations
           └─> Views more materials
               └─> Decides on selection

3. CONVERSION
   └─> Creates contract
       └─> Reviews and signs
           └─> Downloads PDF
               └─> Contract assigned to installer

4. TRACKING
   └─> Receives installation date
       └─> Tracks progress in real-time
           └─> Views installation photos
               └─> Project completed ✅
```

### Sales Rep Journey: From Login to Client Management

```
┌─────────────────────────────────────────────────────────────────┐
│                 SALES REP USER JOURNEY                          │
└─────────────────────────────────────────────────────────────────┘

1. MORNING ROUTINE
   └─> Logs in → Dashboard overview
       └─> Checks new messages in inbox
           └─> Reviews active projects
               └─> Plans day

2. CLIENT INTERACTION
   └─> Responds to client messages
       └─> Provides material recommendations
           └─> Answers questions via chat
               └─> Schedules consultation

3. PROJECT MANAGEMENT
   └─> Creates contract for client
       └─> Assigns installer
           └─> Monitors installation progress
               └─> Updates client

4. ANALYTICS & OPTIMIZATION
   └─> Reviews daily/weekly analytics
       └─> Identifies trends
           └─> Adjusts strategy
```

---

## 📋 Table of Contents

1. [Getting Started](#getting-started)
2. [User Personas](#user-personas)
3. [User Journey Maps](#user-journey-maps)
4. [Client Guide](#client-guide)
5. [Sales Representative Guide](#sales-representative-guide)
6. [Installer Guide](#installer-guide)
7. [Scheduler Guide](#scheduler-guide)
8. [Admin Guide](#admin-guide)
9. [Common Features](#common-features)
10. [Troubleshooting](#troubleshooting)
11. [Design Patterns & Best Practices](#design-patterns--best-practices)

---

## 🚀 Getting Started

### Download & Installation

**iOS:**
- Download from the [App Store](https://apps.apple.com/app/absolute-stone-design)
- Requires iOS 14.0 or later

**Android:**
- Download from [Google Play Store](https://play.google.com/store/apps/details?id=com.JohnColani.asdapp)
- Requires Android 8.0 (API level 26) or later

**Web:**
- Visit: https://absolute-stone-design-app.web.app
- Works on all modern browsers (Chrome, Safari, Firefox, Edge)

### First-Time Setup

1. **Launch the App**
   - On mobile: Open the app from your home screen
   - On web: Visit the web app URL

2. **Sign Up or Continue as Guest**
   - **Web Users**: Can browse immediately without signing up
   - **Mobile Users**: Will see an onboarding screen with option to "Continue as Guest"
   - To access premium features (chat, contracts, profile), you'll need to sign up

3. **Create Your Account**
   - Tap "Sign Up" or "Get Started"
   - Enter your email and password
   - Or sign in with Google/Apple (iOS only)
   - Complete your profile with name and contact information

4. **Grant Permissions** (Mobile Only)
   - Allow notifications to receive updates about your projects
   - Allow location access for map features (optional)
   - Allow camera access to upload photos (optional)

---

## 👤 Client Guide

### Overview

As a **Client**, you can browse materials, chat with sales representatives, create contracts, and track your installation progress.

### Key Features

#### 1. **Browse Materials** 🏠

**Access:** Home tab (bottom navigation)

**Features:**
- View trending materials
- Browse new arrivals
- Explore popular selections
- Check limited-time offers
- Filter by material type (Granite, Marble, Quartz)
- Search for specific materials

**How to Use:**
1. Open the app and tap the **Home** tab
2. Scroll through featured collections
3. Tap any material card to view details
4. Use the search icon to find specific materials
5. Filter by category using the category buttons

#### 2. **Chat with Sales Representatives** 💬

**Access:** Chat tab (bottom navigation) or from material details

**Features:**
- Real-time messaging with sales reps
- Send voice messages
- Share images
- View conversation history
- Get instant responses

**How to Use:**
1. Tap the **Chat** tab
2. Browse available sales representatives
3. Tap on a sales rep to start a conversation
4. Type your message or use the microphone icon for voice messages
5. Tap the camera icon to share photos
6. View your conversation history anytime

**Note:** You must be signed in to chat with sales reps.

#### 3. **AI Assistant (Amy)** 🤖

**Access:** Chat tab → "Chat with Amy" button

**Features:**
- 24/7 instant customer support
- Answers questions about materials, installation, and services
- Shows relevant material images
- Personalized greetings
- Conversation history

**How to Use:**
1. Go to the **Chat** tab
2. Tap "Chat with Amy"
3. Ask any question about:
   - Material types and properties
   - Installation processes
   - Pricing information
   - Maintenance tips
   - Design recommendations
4. Amy will provide instant, accurate responses with images

#### 4. **Create Contracts** 📄

**Access:** Profile tab → "My Contracts" or from sales rep chat

**Features:**
- Digital contract creation
- Electronic signatures
- PDF generation and download
- Contract tracking
- Status updates

**How to Use:**
1. Navigate to **Profile** tab
2. Tap "My Contracts" or "Create Contract"
3. Fill in contract details:
   - Project description
   - Material selection
   - Installation address
   - Timeline
   - Special requirements
4. Review and sign electronically
5. Download PDF for your records
6. Track contract status in real-time

#### 5. **Track Installations** 🔧

**Access:** Profile tab → "My Projects" or from contract details

**Features:**
- Real-time installation progress
- Timeline visualization
- Photo albums from installation site
- Installer information
- Status updates

**How to Use:**
1. Go to **Profile** tab
2. Tap "My Projects" or select a contract
3. View installation timeline:
   - **Scheduled**: Installation date set
   - **In Progress**: Installation underway
   - **Completed**: Installation finished
4. Browse photo albums from the installation
5. Contact installer if needed

#### 6. **View Map** 🗺️

**Access:** Map tab (bottom navigation)

**Features:**
- View showroom locations
- Find nearby installers
- Get directions
- View business hours

**How to Use:**
1. Tap the **Map** tab
2. View pinned locations
3. Tap a location for details
4. Get directions using your device's map app

#### 7. **Search Materials** 🔍

**Access:** Search tab (bottom navigation)

**Features:**
- Search by material name
- Filter by type, color, finish
- Advanced search options
- Save favorite searches

**How to Use:**
1. Tap the **Search** tab
2. Enter keywords in the search bar
3. Use filters to narrow results
4. Tap a result to view details
5. Save favorites for later

#### 8. **Profile Management** 👤

**Access:** Profile tab (bottom navigation)

**Features:**
- Edit personal information
- Upload profile photo
- Change password
- Notification settings
- App preferences

**How to Use:**
1. Tap the **Profile** tab
2. Tap "Edit Profile"
3. Update your information
4. Tap "Save" to apply changes

---

## 💼 Sales Representative Guide

### Overview

As a **Sales Representative**, you manage clients, view projects, track analytics, and communicate with clients through the chat inbox.

### Key Features

#### 1. **Dashboard Overview** 📊

**Access:** Main dashboard (automatically shown when logged in as Sales Rep)

**Features:**
- Total clients count
- Active projects
- Recent activity
- Quick actions
- Performance statistics

**How to Use:**
1. Log in with your sales rep account
2. View dashboard statistics at a glance
3. Use quick action cards for common tasks

#### 2. **Client Management** 👥

**Access:** Dashboard → "My Clients" tab or drawer menu

**Features:**
- View all assigned clients
- Client contact information
- Client project history
- Communication history
- Client status tracking

**How to Use:**
1. Open the drawer menu (☰) or tap "My Clients" tab
2. Browse your client list
3. Tap a client to view:
   - Contact details
   - Project history
   - Chat conversations
   - Contract status
4. Start a new conversation or view existing chats

#### 3. **Project Management** 📁

**Access:** Dashboard → "Projects" tab or drawer menu

**Features:**
- View all client projects
- Project status tracking
- Contract details
- Installation progress
- Timeline visualization

**How to Use:**
1. Navigate to "Projects" tab
2. View projects by status:
   - **Draft**: Contracts being created
   - **Pending**: Awaiting client signature
   - **Active**: Installation in progress
   - **Completed**: Finished projects
3. Tap a project for detailed view
4. Update project status as needed

#### 4. **Chat Inbox** 💬

**Access:** Dashboard → "Chat Inbox" or drawer menu → "Chat Inbox"

**Features:**
- View all client conversations
- Real-time messaging
- Voice message support
- Image sharing
- Unread message indicators
- Conversation search

**How to Use:**
1. Open "Chat Inbox" from dashboard or drawer
2. View all active conversations
3. Tap a conversation to open
4. Respond to client messages
5. Use voice messages for quick responses
6. Share images of materials or installations

#### 5. **Analytics Dashboard** 📈

**Access:** Dashboard → "Analytics" tab

**Features:**
- Sales performance metrics
- Client conversion rates
- Project completion statistics
- Revenue tracking
- Monthly/quarterly reports

**How to Use:**
1. Navigate to "Analytics" tab
2. View key performance indicators
3. Filter by time period (week, month, quarter)
4. Export reports if needed

#### 6. **Settings** ⚙️

**Access:** Dashboard → "Settings" tab or drawer menu

**Features:**
- Profile management
- Notification preferences
- Availability status
- Contact information
- App preferences

**How to Use:**
1. Go to "Settings" tab
2. Update your profile information
3. Configure notification settings
4. Set availability status
5. Save changes

---

## 🔧 Installer Guide

### Overview

As an **Installer**, you manage active jobs, track your work history, update job status, and communicate with clients and sales reps.

### Key Features

#### 1. **Dashboard Overview** 📊

**Access:** Main dashboard (automatically shown when logged in as Installer)

**Features:**
- Active jobs count
- Job history
- Availability status
- Quick actions
- Performance metrics

**How to Use:**
1. Log in with your installer account
2. View dashboard at a glance
3. Check active job count
4. Toggle availability status

#### 2. **Active Jobs** 🛠️

**Access:** Dashboard → "Active Jobs" tab or drawer menu

**Features:**
- List of assigned installations
- Job details and location
- Client information
- Installation timeline
- Photo upload capability
- Status updates

**How to Use:**
1. Navigate to "Active Jobs" tab
2. View all assigned jobs
3. Tap a job to view details:
   - Client name and contact
   - Installation address
   - Material specifications
   - Timeline and deadlines
4. Update job status:
   - **Scheduled**: Job is confirmed
   - **In Progress**: Currently working
   - **Completed**: Installation finished
5. Upload photos:
   - Tap "Add Photos" button
   - Take photos or select from gallery
   - Add captions if needed
   - Photos are visible to clients

#### 3. **Job History** 📜

**Access:** Dashboard → "Job History" tab or drawer menu

**Features:**
- Completed installations
- Past job details
- Photo albums
- Client feedback
- Performance tracking

**How to Use:**
1. Go to "Job History" tab
2. Browse completed jobs
3. View job details and photos
4. Review client information
5. Use for reference on similar projects

#### 4. **Availability Management** ✅

**Access:** Dashboard → Profile or Settings

**Features:**
- Set availability status (Available/Busy)
- Update maximum job capacity
- Location tracking (optional)
- Schedule management

**How to Use:**
1. Open your profile or settings
2. Toggle "Available" status
3. Update maximum jobs you can handle
4. Set your location (optional)
5. Save changes

**Note:** When you're marked as "Busy" or at capacity, you won't receive new job assignments.

#### 5. **Profile Management** 👤

**Access:** Dashboard → Profile or drawer menu

**Features:**
- Edit personal information
- Update specialization
- Add skills and experience
- Upload profile photo
- Vehicle information
- Rating and reviews

**How to Use:**
1. Navigate to your profile
2. Tap "Edit Profile"
3. Update:
   - Name and contact information
   - Specialization (e.g., "Kitchen Countertops", "Bathroom Vanities")
   - Years of experience
   - Skills list
   - Vehicle type
4. Upload a professional photo
5. Save changes

#### 6. **Job Assignment Notifications** 🔔

**Features:**
- Push notifications for new assignments
- Assignment request details
- Accept/decline options
- Match score information

**How to Use:**
1. Receive notification when assigned a job
2. Review assignment details
3. Check match score (how well the job fits your skills)
4. Accept or decline the assignment
5. Add notes if declining

---

## 📅 Scheduler Guide

### Overview

As a **Scheduler**, you manage calendar events, create templates, schedule installer appointments, service orders, and pickups using Google Calendar integration.

### Key Features

#### 1. **Dashboard Overview** 📊

**Access:** Main dashboard (automatically shown when logged in as Scheduler)

**Features:**
- Calendar view
- Event type filters
- Quick event creation
- Upcoming events list
- Event statistics

**How to Use:**
1. Log in with your scheduler account
2. View calendar dashboard
3. See upcoming events at a glance
4. Use tabs to filter by event type

#### 2. **Event Types** 📋

The scheduler manages four types of events:

**a. Templates (Templator)**
- Reusable event templates
- Standard appointment types
- Quick event creation

**b. Installer Appointments**
- Installer job assignments
- Installation scheduling
- Client and installer information

**c. Service Orders**
- Service and maintenance appointments
- Follow-up visits
- Repair scheduling

**d. Pickups**
- Material pickup scheduling
- Delivery coordination
- Warehouse pickups

#### 3. **Create Events** ➕

**Access:** Dashboard → Tap "+" (FAB) button

**Features:**
- Full-screen event creation dialog
- Event type selection
- Date and time picker
- Client information
- Location details
- Description and notes
- Google Calendar sync

**How to Use:**
1. Tap the "+" (Floating Action Button) on any event tab
2. Select event type:
   - **Template**: Choose from existing templates
   - **Installer**: Assign to an installer
   - **Service Order**: Create service appointment
   - **Pickup**: Schedule material pickup
3. Fill in event details:
   - **Summary**: Event title
   - **Start Date & Time**: When the event begins
   - **End Date & Time**: When the event ends
   - **Location**: Installation or service address
   - **Description**: Additional notes
   - **Client**: Select or enter client name
4. Tap "Create Event"
5. Event is automatically synced to Google Calendar

#### 4. **View Events** 👁️

**Access:** Dashboard → Event tabs (Templates, Installer, Service, Pickup)

**Features:**
- Filtered event lists by type
- Color-coded event indicators
- Event details view
- Client information extraction
- Date and time display

**How to Use:**
1. Select an event type tab:
   - **Templates**: View template events
   - **Installer**: View installer appointments
   - **Service**: View service orders
   - **Pickup**: View pickup schedules
2. Browse events in chronological order
3. Tap an event to view full details
4. See client name, location, and description

#### 5. **Edit Events** ✏️

**Access:** Event details → "Edit" button

**Features:**
- Update event information
- Change date/time
- Modify location
- Update description
- Change event type

**How to Use:**
1. Open an event from the list
2. Tap "Edit" button
3. Modify any field
4. Tap "Save" to update
5. Changes sync to Google Calendar

#### 6. **Delete Events** 🗑️

**Access:** Event details → "Delete" button

**Features:**
- Remove events from calendar
- Google Calendar sync
- Confirmation dialog

**How to Use:**
1. Open an event
2. Tap "Delete" button
3. Confirm deletion
4. Event is removed from app and Google Calendar

#### 7. **Filter Events** 🔍

**Features:**
- Filter by event type using tabs
- Color-coded indicators:
   - **Templates**: Blue
   - **Installer**: Green
   - **Service**: Orange
   - **Pickup**: Purple

**How to Use:**
1. Use tabs at the top to filter events
2. Each tab shows only that event type
3. Events are color-coded for easy identification

#### 8. **Google Calendar Integration** 📅

**Features:**
- Automatic sync with Google Calendar
- Real-time updates
- Calendar access verification
- Event creation in Google Calendar

**Setup:**
1. Ensure Google Calendar service account is configured
2. Calendar must be shared with service account email
3. Calendar ID must be set in app configuration

**How to Use:**
1. All events created in the app automatically appear in Google Calendar
2. Events edited in the app sync to Google Calendar
3. Events deleted in the app are removed from Google Calendar
4. View events in Google Calendar app or web interface

---

## 👨‍💼 Admin Guide

### Overview

As an **Admin**, you have full system access to manage users, materials, content, analytics, notifications, and system settings.

### Key Features

#### 1. **Dashboard Overview** 📊

**Access:** Main dashboard (automatically shown when logged in as Admin)

**Features:**
- Total users count
- Sales reps count
- Installers count
- Guest users count
- Contracts count
- Active jobs count
- Quick actions
- Statistics cards

**How to Use:**
1. Log in with your admin account
2. View dashboard statistics
3. Use quick action cards for common tasks
4. Monitor platform activity

#### 2. **User Management** 👥

**Access:** Dashboard → "User Management" tab

**Features:**
- View all users (clients, sales reps, installers, schedulers)
- Promote users to different roles
- Demote users
- Delete users
- View user details
- Filter by role

**How to Use:**
1. Navigate to "User Management" tab
2. Browse all users
3. Filter by role if needed
4. Tap a user to view details
5. Use action buttons to:
   - **Promote**: Change user role (e.g., client → sales rep)
   - **Demote**: Remove role privileges
   - **Delete**: Remove user account
6. Confirm actions when prompted

#### 3. **Sales Rep Management** 💼

**Access:** Dashboard → "User Management" → Sales Reps section

**Features:**
- Add new sales representatives
- Edit sales rep information
- View sales rep performance
- Assign clients to sales reps
- Remove sales reps

**How to Use:**
1. Go to "User Management" tab
2. Navigate to "Sales Reps" section
3. Tap "Add Sales Rep" to create new
4. Fill in information:
   - Name
   - Email
   - Phone
   - Rating
   - Number of reviews
5. Tap "Save"
6. Edit or remove existing sales reps as needed

#### 4. **Installer Management** 🔧

**Access:** Dashboard → "User Management" → Installers section

**Features:**
- Add new installers
- Edit installer profiles
- Set availability status
- Manage installer skills
- View installer ratings
- Assign jobs to installers

**How to Use:**
1. Navigate to "User Management" → "Installers"
2. Tap "Add Installer" to create new
3. Fill in installer details:
   - Name and contact information
   - Specialization
   - Experience level
   - Skills
   - Vehicle information
   - Maximum jobs capacity
4. Set availability status
5. Save changes

#### 5. **Scheduler Management** 📅

**Access:** Dashboard → "User Management" → Schedulers section

**Features:**
- Add new schedulers
- Edit scheduler information
- Manage calendar access
- View scheduler activity

**How to Use:**
1. Go to "User Management" → "Schedulers"
2. Add or edit schedulers
3. Ensure Google Calendar access is configured
4. Monitor scheduler activity

#### 6. **Content Management** 🖼️

**Access:** Dashboard → "Content Management" tab or Main tab

**Features:**
- Upload material images
- Manage trending images
- Manage new arrivals
- Manage popular materials
- Manage limited offers
- Delete images
- Set image titles

**How to Use:**
1. Navigate to "Content Management" or Main tab
2. Select image category:
   - **Recommended Images**: Featured materials
   - **Trending Images**: Popular materials
   - **New Images**: Latest arrivals
   - **Popular Images**: Most viewed
   - **Limited Images**: Limited-time offers
3. Tap "Upload Image" button
4. Select image from device
5. Enter image title
6. Tap "Upload"
7. Delete images by tapping the delete icon

#### 7. **Contract Management** 📄

**Access:** Dashboard → "Contracts" section

**Features:**
- View all contracts
- Filter by status
- View contract details
- Download contract PDFs
- Monitor contract progress

**How to Use:**
1. Navigate to "Contracts" section
2. Browse all contracts
3. Filter by status (Draft, Pending, Active, Completed)
4. Tap a contract to view details
5. Download PDF if needed
6. Monitor installation progress

#### 8. **Notification Management** 📢

**Access:** Dashboard → Main tab → "Send Notification" section

**Features:**
- Send notifications to all users
- Send notifications to specific roles
- Notification history
- Version update notifications
- Custom notification messages

**How to Use:**
1. Go to Main tab
2. Find "Send Notification" section
3. Enter notification:
   - **Title**: Notification headline
   - **Message**: Notification body text
   - **Target**: All users or specific role
4. Tap "Send Notification"
5. Wait for confirmation (may take up to 90 seconds)
6. View notification history

**Note:** Notifications are sent via push notifications and work even when the app is closed.

#### 9. **Version Update Notifications** 🚀

**Access:** Dashboard → Settings tab → Version Update section

**Features:**
- Send version update notifications
- Target specific user roles
- Force update option
- Update message customization

**How to Use:**
1. Navigate to Settings tab
2. Find "Version Update" section
3. Enter:
   - **New Version**: Version number (e.g., "3.0.18")
   - **Update Message**: What's new in this version
   - **Target Roles**: Select roles to notify
   - **Force Update**: Require users to update
4. Tap "Send Version Update"
5. Users will receive notification about the update

#### 10. **Amy AI Assistant Management** 🤖

**Access:** Dashboard → "Amy AI Manager" or drawer menu

**Features:**
- View all client conversations with Amy
- Review conversation history
- Manage knowledge base
- Add/edit Q&A pairs
- Test AI responses
- Monitor AI usage

**How to Use:**
1. Navigate to "Amy AI Manager" from dashboard or drawer
2. View all conversations
3. Tap a conversation to review
4. Go to "Knowledge Base" to manage Q&A pairs
5. Add new questions and answers
6. Edit existing entries
7. Delete outdated information

#### 11. **Guest User Management** 👤

**Access:** Dashboard → "Guest Users" section

**Features:**
- View all guest users
- Convert guests to registered users
- Clean up inactive guests
- Monitor guest activity

**How to Use:**
1. Navigate to "Guest Users" section
2. Browse guest user list
3. View guest activity
4. Convert to registered user if needed
5. Clean up inactive guests

#### 12. **Analytics & Statistics** 📈

**Access:** Dashboard → "Analytics" tab

**Features:**
- User growth statistics
- Role distribution
- Active users count
- Contract statistics
- Installation statistics
- Platform usage metrics

**How to Use:**
1. Go to "Analytics" tab
2. View key metrics
3. Filter by time period
4. Export reports if needed

#### 13. **Settings** ⚙️

**Access:** Dashboard → "Settings" tab or drawer menu

**Features:**
- App version information
- System configuration
- Firebase configuration
- Notification settings
- Version update management
- FCM token debugging

**How to Use:**
1. Navigate to Settings tab
2. View app version and build number
3. Configure system settings
4. Manage version updates
5. Debug FCM tokens if needed

---

## 🔄 Common Features

### Profile Management

**All Users:**
1. Navigate to Profile tab or drawer menu
2. Tap "Edit Profile"
3. Update:
   - Name
   - Email
   - Phone number
   - Address
   - Profile photo
4. Save changes

### Notifications

**All Users:**
- Receive push notifications for:
  - New messages
  - Contract updates
  - Installation status changes
  - Admin announcements
  - Version updates
- Manage notification preferences in Settings

### Search

**All Users:**
- Use search to find:
  - Materials
  - Sales representatives
  - Installers
  - Contracts
  - Events (Schedulers)

### Help & Support

**All Users:**
- Chat with Amy AI assistant for instant help
- Contact sales representatives via chat
- View app documentation
- Contact admin for technical issues

---

## 🔧 Troubleshooting

### Common Issues

#### 1. **Can't Sign In**
- **Problem**: Unable to log in with email/password
- **Solutions**:
  - Check internet connection
  - Verify email and password are correct
  - Try "Forgot Password" to reset
  - Clear app cache and try again

#### 2. **Notifications Not Working**
- **Problem**: Not receiving push notifications
- **Solutions**:
  - Check notification permissions in device settings
  - Ensure app notifications are enabled
  - Check FCM token is valid (Admin can verify)
  - Reinstall app if needed

#### 3. **Chat Messages Not Sending**
- **Problem**: Messages stuck or not delivered
- **Solutions**:
  - Check internet connection
  - Verify recipient is online
  - Try refreshing the chat
  - Restart the app

#### 4. **Calendar Events Not Syncing** (Schedulers)
- **Problem**: Events not appearing in Google Calendar
- **Solutions**:
  - Verify Google Calendar service account is configured
  - Check calendar is shared with service account email
  - Verify calendar ID is correct
  - Check Google Calendar API permissions

#### 5. **Images Not Loading**
- **Problem**: Material images not displaying
- **Solutions**:
  - Check internet connection
  - Clear app cache
  - Try refreshing the page
  - Contact admin if issue persists

#### 6. **App Crashes**
- **Problem**: App closes unexpectedly
- **Solutions**:
  - Update to latest app version
  - Clear app cache
  - Restart device
  - Reinstall app if needed
  - Contact support with error details

#### 7. **Can't Upload Photos** (Installers)
- **Problem**: Unable to upload installation photos
- **Solutions**:
  - Check camera/storage permissions
  - Verify internet connection
  - Check available storage space
  - Try selecting from gallery instead

### Getting Help

1. **Amy AI Assistant**: Ask Amy for help with common questions
2. **Sales Representatives**: Chat with a sales rep for assistance
3. **Admin Support**: Contact admin for technical issues
4. **Documentation**: Check this guide and other docs in the app

---

## 📞 Support Contacts

- **Technical Support**: Contact admin through the app
- **Sales Inquiries**: Chat with sales representatives
- **Installation Questions**: Contact your assigned installer
- **Scheduling Issues**: Contact scheduler or admin

---

## 🔄 App Updates

### Checking for Updates

**iOS:**
- Updates are available through the App Store
- You'll receive a notification when an update is available
- Go to App Store → Updates to install

**Android:**
- Updates are available through Google Play Store
- You'll receive a notification when an update is available
- Go to Play Store → My Apps → Updates to install

**Web:**
- Web app updates automatically
- Refresh your browser to get the latest version

### Version Update Notifications

Admins can send version update notifications to inform users about new features and improvements. You'll receive a push notification when an update is available.

**Force Updates:**
- Some updates may be marked as "Force Update"
- You must update the app to continue using it
- Follow the update prompt to install the new version

---

## 📱 Platform-Specific Notes

### iOS
- Requires iOS 14.0 or later
- Supports Apple Sign-In
- Optimized for iPhone and iPad
- Native iOS design elements

### Android
- Requires Android 8.0 (API level 26) or later
- Material Design components
- Supports Google Sign-In
- Optimized for phones and tablets

### Web
- Works on all modern browsers
- Responsive design for desktop and mobile
- Can browse without signing up
- Full feature set available after sign-in

---

## 🔐 Security & Privacy

### Data Protection
- All data is encrypted in transit
- User authentication via Firebase
- Role-based access control
- Secure file uploads

### Privacy
- Your personal information is protected
- Only authorized users can view your data
- Chat conversations are private
- Contract information is secure

### Best Practices
- Use strong passwords
- Don't share your account
- Log out on shared devices
- Report suspicious activity to admin

---

## 📚 Additional Resources

- **App Documentation**: Available in the app
- **Video Tutorials**: Coming soon
- **FAQ Section**: Ask Amy for common questions
- **Release Notes**: View in app settings

---

## 🎨 Design Patterns & Best Practices

### Visual Design Language

**Color Coding:**
- 🔵 **Blue**: Primary actions, navigation
- 🟢 **Green**: Success states, completed items
- 🟠 **Orange**: Warnings, pending items
- 🔴 **Red**: Errors, urgent items
- 🟣 **Purple**: Premium features, admin functions

**Icon System:**
- 🏠 Home/Materials
- 💬 Chat/Messages
- 📄 Contracts/Documents
- 🔧 Installation/Jobs
- 📅 Calendar/Events
- 👤 Profile/User
- ⚙️ Settings
- 📊 Analytics

### Interaction Patterns

**Navigation:**
- Bottom navigation for main sections (Mobile)
- Drawer menu for role-specific features
- Tab navigation for filtered views
- Floating Action Button (FAB) for primary actions

**Feedback:**
- Loading indicators for async operations
- Success/error messages with clear actions
- Progress indicators for multi-step processes
- Toast notifications for quick confirmations

**Error Prevention:**
- Confirmation dialogs for destructive actions
- Form validation with inline feedback
- Auto-save for draft content
- Clear error messages with solutions

### Accessibility

**Design Considerations:**
- High contrast text for readability
- Large touch targets (minimum 44x44px)
- Clear visual hierarchy
- Screen reader support
- Keyboard navigation (Web)

**Best Practices:**
- Use descriptive button labels
- Provide alt text for images
- Ensure color is not the only indicator
- Support text scaling

---

## 📊 Feature Comparison Matrix

| Feature | Client | Sales Rep | Installer | Scheduler | Admin |
|---------|:------:|:---------:|:---------:|:---------:|:-----:|
| Browse Materials | ✅ | ✅ | ✅ | ✅ | ✅ |
| Chat with Sales Rep | ✅ | ✅ | ❌ | ❌ | ✅ |
| Create Contracts | ✅ | ✅ | ❌ | ❌ | ✅ |
| Track Installations | ✅ | ✅ | ✅ | ❌ | ✅ |
| Manage Clients | ❌ | ✅ | ❌ | ❌ | ✅ |
| Manage Jobs | ❌ | ❌ | ✅ | ❌ | ✅ |
| Calendar Events | ❌ | ❌ | ❌ | ✅ | ✅ |
| User Management | ❌ | ❌ | ❌ | ❌ | ✅ |
| Content Management | ❌ | ❌ | ❌ | ❌ | ✅ |
| Analytics | ❌ | ✅ | ❌ | ❌ | ✅ |
| Notifications | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 🔄 State Management & Data Flow

### Client Data Flow

```
User Action → BLoC Event → Repository → Data Source → Firebase
                ↓
            State Update → UI Rebuild → User Feedback
```

### Real-time Updates

- **Chat Messages**: Real-time via Firestore streams
- **Contract Status**: Real-time updates
- **Installation Progress**: Live photo uploads
- **Calendar Events**: Google Calendar sync
- **Notifications**: Push notifications via FCM

---

## 🎯 Task-Oriented Quick Reference

### "I want to..."

**Find a material:**
1. Open Home tab
2. Browse collections or use Search
3. Tap material card for details

**Talk to a sales rep:**
1. Go to Chat tab
2. Browse sales reps
3. Tap to start conversation

**Create a contract:**
1. Profile tab → "My Contracts"
2. Tap "Create Contract"
3. Fill details and sign

**Track my installation:**
1. Profile tab → "My Projects"
2. Select project
3. View timeline and photos

**Manage my clients** (Sales Rep):
1. Dashboard → "My Clients"
2. Browse or search clients
3. Tap for details

**Update job status** (Installer):
1. Dashboard → "Active Jobs"
2. Select job
3. Update status and add photos

**Create calendar event** (Scheduler):
1. Dashboard → Select event type tab
2. Tap "+" button
3. Fill event details

**Send notification** (Admin):
1. Dashboard → Main tab
2. "Send Notification" section
3. Enter title/message and send

---

## 💡 Pro Tips

### For Clients
- 💡 Use Amy AI assistant for quick questions before chatting with sales rep
- 💡 Save favorite materials by taking screenshots
- 💡 Enable notifications to never miss installation updates
- 💡 Check map for showroom locations and hours

### For Sales Reps
- 💡 Use analytics to identify best-performing materials
- 💡 Set up quick replies for common questions
- 💡 Check chat inbox first thing in the morning
- 💡 Use voice messages for faster responses

### For Installers
- 💡 Update availability status regularly
- 💡 Upload photos immediately after completing work
- 💡 Use location tracking for accurate ETAs
- 💡 Keep job history for reference on similar projects

### For Schedulers
- 💡 Create templates for recurring event types
- 💡 Use color coding to quickly identify event types
- 💡 Sync regularly with Google Calendar
- 💡 Set reminders for important appointments

### For Admins
- 💡 Check analytics weekly for trends
- 💡 Send notifications during off-peak hours
- 💡 Review Amy conversations for common questions
- 💡 Keep knowledge base updated

---

**Last Updated**: January 2026  
**App Version**: 3.0.17  
**Documentation Version**: 2.0 (Product Designer Enhanced)

---

*This guide follows product design principles: user-centered, visually scannable, and task-oriented. For the most up-to-date information, please refer to the in-app help or contact your administrator.*
