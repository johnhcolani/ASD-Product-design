# Absolute Stone Design - Design System

Comprehensive design system documentation for iOS, Android, and Web platforms.

**Version:** 3.0.17+81  
**Last Updated:** January 2026  
**Platforms:** iOS, Android, Web (Flutter)

---

## 🎨 Visual Showcase

### Complete Color Palette

#### Primary Colors & Dashboard

| Color | Hex | RGB | Usage | Preview |
|-------|-----|-----|-------|---------|
| **Dashboard Dark** | `#0A081E` | RGB(10, 8, 30) | Main dark background for dashboards | ⬛⬛⬛⬛⬛ |
| **Dashboard Secondary** | `#1A1A2E` | RGB(26, 26, 46) | Secondary dark background | ⬛⬛⬛⬛⬛ |
| **Dashboard Tertiary** | `#0F0F1A` | RGB(15, 15, 26) | Tertiary dark background | ⬛⬛⬛⬛⬛ |
| **App Blue** | `#3C2C8D` | RGB(60, 44, 141) | Primary app blue | 🟦🟦🟦🟦🟦 |
| **Gradient Start** | `#0A081E` | RGB(10, 8, 30) | Gradient start (dark blue-purple) | ⬛⬛⬛⬛⬛ |
| **Gradient End** | `#413EC1` | RGB(65, 62, 193) | Gradient end (purple) | 🟦🟦🟦🟦🟦 |
| **Gradient Secondary** | `#5657A8` | RGB(86, 87, 168) | Secondary gradient color | 🟦🟦🟦🟦🟦 |
| **Dark Gradient Start** | `#0A0A28` | RGB(10, 10, 40) | Dark gradient start | ⬛⬛⬛⬛⬛ |
| **Dark Gradient End** | `#2A28A4` | RGB(42, 40, 164) | Dark gradient end | 🟦🟦🟦🟦🟦 |
| **Light Gradient Start** | `#E0E0F8` | RGB(224, 224, 248) | Light gradient start | ⬜⬜⬜⬜⬜ |
| **Light Gradient End** | `#A0A0FF` | RGB(160, 160, 255) | Light gradient end | 🟦🟦🟦🟦🟦 |

#### Semantic Colors (Status Indicators)

| Status | Hex | RGB | Usage | Emoji |
|--------|-----|-----|-------|-------|
| ✅ **Success** | `#43A047` | RGB(67, 160, 71) | Success state (Green 600) | 🟢 |
| ⚠️ **Warning** | `#FB8C00` | RGB(251, 140, 0) | Warning state (Orange 600) | 🟠 |
| ❌ **Error** | `#E53935` | RGB(229, 57, 53) | Error state (Red 600) | 🔴 |
| ℹ️ **Info** | `#1E88E5` | RGB(30, 136, 229) | Info state (Blue 600) | 🔵 |
| ⏳ **Pending** | `#FFB74D` | RGB(255, 183, 77) | Pending state (Orange 300) | 🟡 |

#### Blue Scale (Primary Actions)

| Color | Hex | RGB | Usage | Preview |
|-------|-----|-----|-------|---------|
| **Blue 50** | `#E3F2FD` | RGB(227, 242, 253) | Very light blue (subtle backgrounds) | ⬜⬜⬜⬜⬜ |
| **Blue 100** | `#BBDEFB` | RGB(187, 222, 251) | Light blue (subtle backgrounds) | ⬜⬜⬜⬜⬜ |
| **Blue 300** | `#64B5F6` | RGB(100, 181, 246) | Light blue (selected items, icons) | 🟦🟦🟦🟦🟦 |
| **Blue 400** | `#42A5F5` | RGB(66, 165, 245) | Medium blue (buttons, links) | 🟦🟦🟦🟦🟦 |
| **Blue 600** | `#1E88E5` | RGB(30, 136, 229) | Darker blue (primary actions) | 🟦🟦🟦🟦🟦 |
| **Blue 700** | `#1976D2` | RGB(25, 118, 210) | Dark blue (emphasis) | 🟦🟦🟦🟦🟦 |
| **Blue 800** | `#1565C0` | RGB(21, 101, 192) | Very dark blue (AppBar, headers) | 🟦🟦🟦🟦🟦 |
| **Blue 900** | `#0D47A1` | RGB(13, 71, 161) | Darkest blue (selected background) | 🟦🟦🟦🟦🟦 |

#### Grey Scale (Text, Borders, Backgrounds)

| Color | Hex | RGB | Usage | Preview |
|-------|-----|-----|-------|---------|
| **Grey 50** | `#FAFAFA` | RGB(250, 250, 250) | Very light grey (backgrounds) | ⬜⬜⬜⬜⬜ |
| **Grey 300** | `#E0E0E0` | RGB(224, 224, 224) | Light grey (borders, disabled) | ⬜⬜⬜⬜⬜ |
| **Grey 400** | `#BDBDBD` | RGB(189, 189, 189) | Medium-light grey | ⬜⬜⬜⬜⬜ |
| **Grey 500** | `#9E9E9E` | RGB(158, 158, 158) | Medium grey | 🩶🩶🩶🩶🩶 |
| **Grey 600** | `#757575` | RGB(117, 117, 117) | Medium-dark grey (text) | 🩶🩶🩶🩶🩶 |
| **Grey 700** | `#616161` | RGB(97, 97, 97) | Dark grey (text) | 🩶🩶🩶🩶🩶 |
| **Grey 800** | `#424242` | RGB(66, 66, 66) | Very dark grey (dropdowns, cards) | 🩶🩶🩶🩶🩶 |

#### Green Scale (Success States, Sales Reps)

| Color | Hex | RGB | Usage | Preview |
|-------|-----|-----|-------|---------|
| **Green 300** | `#81C784` | RGB(129, 199, 132) | Light green (success icons) | 🟢🟢🟢🟢🟢 |
| **Green 600** | `#43A047` | RGB(67, 160, 71) | Medium green (success buttons) | 🟢🟢🟢🟢🟢 |
| **Green 700** | `#388E3C` | RGB(56, 142, 60) | Dark green | 🟢🟢🟢🟢🟢 |

#### Orange Scale (Installers, Warnings)

| Color | Hex | RGB | Usage | Preview |
|-------|-----|-----|-------|---------|
| **Orange 200** | `#FFCC80` | RGB(255, 204, 128) | Very light orange (banners) | 🟠🟠🟠🟠🟠 |
| **Orange 300** | `#FFB74D` | RGB(255, 183, 77) | Light orange (icons, accents) | 🟠🟠🟠🟠🟠 |
| **Orange 600** | `#FB8C00` | RGB(251, 140, 0) | Medium orange (installer badges) | 🟠🟠🟠🟠🟠 |
| **Orange 800** | `#F57C00` | RGB(245, 124, 0) | Dark orange | 🟠🟠🟠🟠🟠 |

#### Purple Scale (Amy AI Assistant)

| Color | Hex | RGB | Usage | Preview |
|-------|-----|-----|-------|---------|
| **Purple 300** | `#BA68C8` | RGB(186, 104, 200) | Light purple (Amy messages) | 🟣🟣🟣🟣🟣 |
| **Purple 600** | `#AB47BC` | RGB(171, 71, 188) | Medium purple (gradients) | 🟣🟣🟣🟣🟣 |
| **Amy Magenta** | `#FFB3F5` | RGB(255, 179, 245) | Light magenta (Amy Manager) | 🟣🟣🟣🟣🟣 |

#### Red Scale (Errors, Delete Actions)

| Color | Hex | RGB | Usage | Preview |
|-------|-----|-----|-------|---------|
| **Red 50** | `#FFEBEE` | RGB(255, 235, 238) | Very light red (error backgrounds) | ⬜⬜⬜⬜⬜ |
| **Red 100** | `#FFCDD2` | RGB(255, 205, 210) | Light red (subtle backgrounds) | 🟥🟥🟥🟥🟥 |
| **Red 300** | `#E57373` | RGB(229, 115, 115) | Light red (error icons) | 🟥🟥🟥🟥🟥 |
| **Red 400** | `#EF5350` | RGB(239, 83, 80) | Medium red (error text) | 🟥🟥🟥🟥🟥 |
| **Red 600** | `#E53935` | RGB(229, 57, 53) | Dark red (error buttons, delete) | 🟥🟥🟥🟥🟥 |
| **Red 700** | `#D32F2F` | RGB(211, 47, 47) | Darker red | 🟥🟥🟥🟥🟥 |

#### White with Opacity

| Color | Hex | RGBA | Usage | Preview |
|-------|-----|------|-------|---------|
| **White** | `#FFFFFF` | RGB(255, 255, 255) | Pure white | ⬜⬜⬜⬜⬜ |
| **White 60** | `#99FFFFFF` | RGBA(255, 255, 255, 0.6) | White with 60% opacity | ⬜⬜⬜⬜⬜ |
| **White 70** | `#B3FFFFFF` | RGBA(255, 255, 255, 0.7) | White with 70% opacity | ⬜⬜⬜⬜⬜ |
| **White 80** | `#CCFFFFFF` | RGBA(255, 255, 255, 0.8) | White with 80% opacity | ⬜⬜⬜⬜⬜ |
| **White 90** | `#E6FFFFFF` | RGBA(255, 255, 255, 0.9) | White with 90% opacity | ⬜⬜⬜⬜⬜ |

#### Text Colors

| Color | Hex | RGB | Usage | Preview |
|-------|-----|-----|-------|---------|
| **Text Light** | `#1A1A1A` | RGB(26, 26, 26) | Text on light backgrounds | ⬛⬛⬛⬛⬛ |
| **Text Dark** | `#F2F2F2` | RGB(242, 242, 242) | Text on dark backgrounds | ⬜⬜⬜⬜⬜ |
| **Placeholder** | `#999999` | RGB(153, 153, 153) | Placeholder text in inputs | 🩶🩶🩶🩶🩶 |

#### Input Colors

| Color | Hex | RGB | Usage | Preview |
|-------|-----|-----|-------|---------|
| **Input Fill Light** | `#F0F0F0` | RGB(240, 240, 240) | Light input background | ⬜⬜⬜⬜⬜ |
| **Input Fill Dark** | `#2A2A40` | RGB(42, 42, 64) | Dark input background | ⬛⬛⬛⬛⬛ |

---

## ✍️ Typography in Action

### Font Family

**Primary Font:** Volte  
**Fallback:** `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`

### Font Weights

| Weight | Value | Usage | Example |
|--------|-------|-------|---------|
| **Light** | 300 | Subtle emphasis | Light text |
| **Regular** | 400 | Body text, default | Regular text |
| **Medium** | 500 | Buttons, labels | Medium text |
| **Semibold** | 600 | Headings, emphasis | Semibold text |
| **Bold** | 700 | Large headings, strong emphasis | **Bold text** |

### Type Scale Examples

#### Headings

| Style | Size | Weight | Line Height | Color | Usage | Example |
|-------|------|--------|-------------|-------|-------|---------|
| **H1** | 32px | Bold (700) | 40px | `#F2F2F2` | Main page titles | <span style="font-size: 32px; font-weight: 700; line-height: 40px; color: #F2F2F2; background: #1a1a1a; padding: 8px 16px; border-radius: 8px; display: inline-block;">The quick brown fox jumps</span> |
| **H2** | 28px | Bold (700) | 36px | `#F2F2F2` | Section headings | <span style="font-size: 28px; font-weight: 700; line-height: 36px; color: #F2F2F2; background: #1a1a1a; padding: 8px 16px; border-radius: 8px; display: inline-block;">The quick brown fox jumps</span> |
| **H3** | 24px | Semibold (600) | 32px | `#F2F2F2` | Subsection headings | <span style="font-size: 24px; font-weight: 600; line-height: 32px; color: #F2F2F2; background: #1a1a1a; padding: 8px 16px; border-radius: 8px; display: inline-block;">The quick brown fox jumps</span> |
| **H4** | 20px | Semibold (600) | 28px | `#F2F2F2` | Card titles, small headings | <span style="font-size: 20px; font-weight: 600; line-height: 28px; color: #F2F2F2; background: #1a1a1a; padding: 8px 16px; border-radius: 8px; display: inline-block;">The quick brown fox jumps</span> |

#### Body Text

| Style | Size | Weight | Line Height | Color | Usage | Example |
|-------|------|--------|-------------|-------|-------|---------|
| **Body Large** | 18px | Regular (400) | 24px | `#F2F2F2` | Large body text, descriptions | <span style="font-size: 18px; font-weight: 400; line-height: 24px; color: #F2F2F2; background: #1a1a1a; padding: 8px 16px; border-radius: 8px; display: inline-block;">The quick brown fox jumps over the lazy dog</span> |
| **Body** | 14px | Regular (400) | 20px | `#F2F2F2` | Default body text | <span style="font-size: 14px; font-weight: 400; line-height: 20px; color: #F2F2F2; background: #1a1a1a; padding: 8px 16px; border-radius: 8px; display: inline-block;">The quick brown fox jumps over the lazy dog</span> |
| **Body Small** | 12px | Regular (400) | 18px | `#F2F2F2` | Secondary text, small descriptions | <span style="font-size: 12px; font-weight: 400; line-height: 18px; color: #F2F2F2; background: #1a1a1a; padding: 8px 16px; border-radius: 8px; display: inline-block;">The quick brown fox jumps over the lazy dog</span> |

#### UI Text

| Style | Size | Weight | Line Height | Color | Usage | Example |
|-------|------|--------|-------------|-------|-------|---------|
| **Button** | 20px | Medium (500) | 28px | White, Underlined | Button text | <span style="font-size: 20px; font-weight: 500; text-decoration: underline; color: #FFFFFF; background: #1a1a1a; padding: 8px 16px; border-radius: 8px; display: inline-block;">LOGIN</span> |
| **Label** | 14px | Medium (500) | 20px | `#1A1A1A` | Form labels | <span style="font-size: 14px; font-weight: 500; line-height: 20px; color: #1A1A1A; background: #fafafa; padding: 8px 16px; border-radius: 8px; display: inline-block; border: 1px solid #e0e0e0;">Email Address</span> |
| **Caption** | 11px | Regular (400) | 15px | `rgba(255,255,255,0.70)` | Captions, metadata | <span style="font-size: 11px; font-weight: 400; line-height: 15px; color: rgba(255,255,255,0.70); background: #1a1a1a; padding: 8px 16px; border-radius: 8px; display: inline-block;">This is caption text</span> |
| **Hint** | 14px | Regular (400) | 20px | `#757575` | Placeholder, hint text | <span style="font-size: 14px; font-weight: 400; line-height: 20px; color: #757575; background: #fafafa; padding: 8px 16px; border-radius: 8px; display: inline-block; border: 1px solid #e0e0e0;">Enter your email address</span> |

---

## 📏 Spacing System

### Base Unit

**4px** - All spacing values are multiples of 4

### Spacing Scale

| Scale | Value | Usage | Visual |
|-------|-------|-------|--------|
| **XS** | 4px | Tight spacing, icons | ▫️▫️▫️▫️▫️ |
| **SM** | 8px | Small spacing, tight margins | ▫️▫️▫️▫️▫️▫️ |
| **MD** | 12px | Medium-small spacing | ▫️▫️▫️▫️▫️▫️▫️ |
| **LG** | 16px | Base spacing (most common) | ▫️▫️▫️▫️▫️▫️▫️▫️ |
| **XL** | 24px | Large spacing, sections | ▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️ |
| **2XL** | 32px | Extra large spacing | ▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️ |
| **3XL** | 48px | XXXL spacing | ▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️ |
| **4XL** | 64px | Maximum spacing | ▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️ |

### Common Spacing Patterns

| Element | Padding | Usage |
|---------|---------|-------|
| **Card** | 16px | Card padding |
| **Button** | 12px 24px (vertical, horizontal) | Button padding |
| **Input Field** | 12px 16px | Input field padding |
| **Dialog** | 24px | Dialog/modal padding |
| **Section** | 32px | Section spacing |
| **Screen** | 24px (mobile), 32px (tablet/web) | Screen padding |

---

## 🔲 Border Radius

### Border Radius Scale

| Name | Value | Usage | Example |
|------|-------|-------|---------|
| **Small** | 4px | Badges, small elements | ▢ (4px) |
| **Medium** | 8px | Small cards, icons | ▢ (8px) |
| **Large** | 12px | Default (buttons, cards, inputs) | ▢ (12px) |
| **XLarge** | 16px | Large cards | ▢ (16px) |
| **XXLarge** | 24px | Modals, dialogs | ▢ (24px) |
| **XL** | 30px | Avatars, special elements | ▢ (30px) |
| **Round** | 50% | Pills, circular elements | ⭕ |

### Most Common Values

| Element | Border Radius | Usage |
|---------|---------------|-------|
| **Buttons** | 12px | RectangularButton, RoundedButton |
| **Cards** | 12px | Material cards, stat cards |
| **Inputs** | 12px | RoundedTextField, text inputs |
| **Modals** | 24px | Dialogs, modals |
| **Avatars** | 30px (for 60px avatar) | Profile pictures |

---

## 🧩 Component Specifications

### Buttons

#### Rectangular Button

| Property | Value | Description |
|----------|-------|-------------|
| **Height** | 50px | Fixed button height |
| **Width** | 90% of screen (mobile) | Button width |
| **Border Radius** | 12px | Rounded corners |
| **Border Width** | 2px | Border thickness |
| **Border Color** | White | Default border color |
| **Font Size** | 20px | Button text size |
| **Font Weight** | Medium (500) | Button text weight |
| **Text Decoration** | Underline | Underlined text |
| **Background** | Transparent | Transparent background |
| **Text Color** | White | White text |

**Example:** `RectangularButton(title: 'LOGIN', backgroundColor: Colors.transparent, textColor: Colors.white)`

#### Rounded Button

| Property | Value | Description |
|----------|-------|-------------|
| **Padding** | 16px 32px | Button padding |
| **Border Radius** | 30px | Fully rounded corners |
| **Background** | White | White background |
| **Text Color** | Black | Black text |
| **Font Size** | 16px | Button text size |
| **Font Weight** | Semibold (600) | Button text weight |
| **Elevation** | 8px | Shadow elevation |

**Example:** `ElevatedButton` with white background and rounded corners

### Input Fields

#### RoundedTextField

| Property | Value | Description |
|----------|-------|-------------|
| **Height** | 48px | Input field height |
| **Padding** | 12px 16px | Input padding |
| **Border Radius** | 12px | Rounded corners |
| **Border** | None | No visible border |
| **Background** | `#F0F0F0` (Light) / `#2A2A40` (Dark) | Input fill color |
| **Icon** | Prefix icon (email, lock, person) | Left side icon |
| **Font Size** | 14px | Text size |
| **Font Weight** | Regular (400) | Text weight |
| **Placeholder Color** | `#999999` (Grey 500) | Placeholder text |

**Example:** `RoundedTextField(hintText: 'Email', icon: Icons.email, controller: controller)`

### Cards

#### Default Card

| Property | Value | Description |
|----------|-------|-------------|
| **Padding** | 16px | Card padding |
| **Border Radius** | 12px | Rounded corners |
| **Background** | `rgba(255, 255, 255, 0.1)` | Glass effect |
| **Border** | `1px solid rgba(255, 255, 255, 0.2)` | Subtle border |
| **Shadow** | Medium shadow | Card elevation |

### Navigation

#### Bottom Navigation

| Property | Value | Description |
|----------|-------|-------------|
| **Items** | 5 items | Home, Chat, Map, Profile, Menu |
| **Height** | 56px (iOS), 60px (Android) | Navigation bar height |
| **Background** | Transparent / Theme-based | Background color |
| **Active Color** | Blue 600 (`#1E88E5`) | Active tab color |
| **Inactive Color** | Grey 600 (`#757575`) | Inactive tab color |

#### Drawer Menu

| Property | Value | Description |
|----------|-------|-------------|
| **Width** | 280px | Drawer width |
| **Background** | `#0A081E` (Dashboard Dark) | Dark background |
| **Header Height** | 160px | Header section height |
| **Item Height** | 48px | Menu item height |
| **Padding** | 16px | Drawer padding |

---

## 🎨 Gradients

### Dashboard Gradient

| Property | Value | Description |
|----------|-------|-------------|
| **Type** | Linear | Linear gradient |
| **Direction** | Top-left to Bottom-right (135°) | Gradient angle |
| **Start Color** | `#0A081E` | Dark blue-purple |
| **End Color** | `#413EC1` | Purple |
| **Usage** | Dashboard backgrounds, drawer headers | Primary gradient |

**CSS:** `linear-gradient(135deg, #0A081E 0%, #413EC1 100%)`

### App Gradient

| Property | Value | Description |
|----------|-------|-------------|
| **Type** | Linear | Linear gradient |
| **Direction** | Center-left to Center-right (90°) | Horizontal gradient |
| **Start Color** | `#0A0A28` | Dark gradient start |
| **End Color** | `#2A28A4` | Dark gradient end |
| **Usage** | App backgrounds, welcome screens | App-wide gradient |

**CSS:** `linear-gradient(90deg, #0A0A28 0%, #2A28A4 100%)`

### Light Gradient

| Property | Value | Description |
|----------|-------|-------------|
| **Type** | Linear | Linear gradient |
| **Direction** | Top-left to Bottom-right | Gradient angle |
| **Start Color** | `#E0E0F8` | Light gradient start |
| **End Color** | `#A0A0FF` | Light gradient end |
| **Usage** | Light theme backgrounds | Light mode gradient |

**CSS:** `linear-gradient(135deg, #E0E0F8 0%, #A0A0FF 100%)`

---

## 🎭 Role-Based Themes

### Admin Dashboard

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| **Primary** | Blue 600 | `#1E88E5` | Primary actions, links |
| **Accent** | Blue 300 | `#64B5F6` | Selected items, icons |
| **Background** | Dashboard Dark | `#0A081E` | Main background |
| **Success** | Green 600 | `#43A047` | Sales rep indicators |
| **Warning** | Orange 600 | `#FB8C00` | Installer badges |
| **Error** | Red 600 | `#E53935` | Error states |

### Client Dashboard

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| **Primary** | App Blue | `#3C2C8D` | Primary branding |
| **Accent** | Light Gradient End | `#A0A0FF` | Accent elements |
| **Background** | Dark Gradient Start | `#0A0A28` | Main background |

### Installer Dashboard

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| **Primary** | Orange 600 | `#FB8C00` | Installer badges, primary actions |
| **Accent** | Orange 300 | `#FFB74D` | Icons, accents |
| **Background** | Dashboard Dark | `#0A081E` | Main background |
| **AppBar** | Blue 800 | `#1565C0` | AppBar background |

### Sales Rep Dashboard

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| **Primary** | Green 600 | `#43A047` | Success indicators, contracts |
| **Accent** | Green 300 | `#81C784` | Icons, accents |
| **Background** | Dashboard Dark | `#0A081E` | Main background |

### Amy AI Assistant

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| **Magenta** | Amy Magenta | `#FFB3F5` | Amy Manager drawer |
| **Purple** | Purple 300 | `#BA68C8` | Amy messages |
| **Cursor** | Amy Cursor | `#D6B4FF` | Cursor color |

---

## 📱 Platform-Specific Guidelines

### iOS

| Element | Specification |
|---------|---------------|
| **Status Bar** | White text on dark background |
| **Navigation** | Native iOS navigation bar |
| **Buttons** | iOS-style button heights (44px minimum) |
| **Font** | Volte or San Francisco (fallback) |
| **Safe Area** | Respect safe area insets |

### Android

| Element | Specification |
|---------|---------------|
| **Status Bar** | White icons on dark background |
| **Navigation** | Material Design bottom navigation |
| **Buttons** | Material button heights (48px minimum) |
| **Font** | Volte or Roboto (fallback) |
| **Status Bar Color** | Transparent with light icons |

### Web

| Element | Specification |
|---------|---------------|
| **Responsive** | Breakpoints: Mobile (360px), Tablet (768px), Desktop (1200px+) |
| **Keyboard Navigation** | Full keyboard support (Tab, Enter, Escape) |
| **Focus States** | Visible focus indicators |
| **Font** | Volte or system font stack |
| **Touch Targets** | Minimum 44x44px |

---

## 🎯 Usage Guidelines

### Color Usage

| ✅ Do | ❌ Don't |
|-------|----------|
| Use semantic colors for status indicators | Create new colors without updating system |
| Use role-specific colors for dashboards | Use colors that don't meet WCAG AA contrast |
| Ensure 4.5:1 contrast for text | Use color alone to convey meaning |
| Test with colorblind simulators | Use arbitrary color values |

### Typography Usage

| ✅ Do | ❌ Don't |
|-------|----------|
| Use established text styles | Use font sizes not in the scale |
| Maintain consistent line heights | Mix font families |
| Use appropriate font weights | Use decorative fonts for body text |
| Follow hierarchy (H1 > H2 > H3) | Skip heading levels |

### Spacing Usage

| ✅ Do | ❌ Don't |
|-------|----------|
| Use 4px base unit system | Use arbitrary spacing values |
| Be consistent with padding/margins | Mix spacing scales |
| Use spacing scale values | Create custom spacing without documentation |
| Maintain visual rhythm | Overcrowd or overspace elements |

---

## 📋 Quick Reference

### Most Used Colors

| Color | Hex | Usage |
|-------|-----|-------|
| **Dashboard Background** | `#0A081E` | Main dashboard background |
| **Primary Blue** | `#1E88E5` | Primary actions, links |
| **Success Green** | `#43A047` | Success states, sales reps |
| **Warning Orange** | `#FB8C00` | Warnings, installers |
| **Error Red** | `#E53935` | Errors, delete actions |
| **Text Dark** | `#F2F2F2` | Text on dark backgrounds |
| **Text Light** | `#1A1A1A` | Text on light backgrounds |

### Most Used Spacing

| Value | Usage |
|-------|-------|
| **4px** | Tight spacing, icons |
| **8px** | Small spacing |
| **12px** | Medium-small spacing |
| **16px** | Base spacing (most common) |
| **24px** | Large spacing, sections |
| **32px** | Extra large spacing |

### Most Used Border Radius

| Value | Usage |
|-------|-------|
| **12px** | Default (buttons, cards, inputs) |
| **24px** | Modals, large cards |
| **30px** | Avatars (for 60px size) |

### Most Used Font Sizes

| Size | Usage |
|------|-------|
| **14px** | Body text (default) |
| **16px** | Medium text |
| **20px** | Buttons, H4 |
| **24px** | H3 |
| **28px** | H2 |
| **32px** | H1 |

---

## 🔧 Implementation

### Flutter Implementation

**Colors:** `lib/core/theme/app_color.dart`
```dart
AppColors.dashboardDark          // #0A081E
AppColors.blue600                // #1E88E5
AppColors.success                // #43A047
AppColors.warning                // #FB8C00
AppColors.error                  // #E53935
```

**Typography:** `lib/features/setting/presentation/app_theme.dart`
```dart
ThemeData.light.textTheme.headline1  // H1: 32px, Bold
ThemeData.light.textTheme.bodyText1  // Body: 14px, Regular
```

**Components:** `lib/core/widgets/`
- `RoundedTextField` - Input fields
- `RectangularButton` - Buttons
- `AppBackground` - Backgrounds

### CSS/Web Implementation

```css
/* Colors */
--color-dashboard-dark: #0A081E;
--color-blue-600: #1E88E5;
--color-success: #43A047;
--color-warning: #FB8C00;
--color-error: #E53935;

/* Typography */
--font-family: 'Volte', -apple-system, BlinkMacSystemFont, sans-serif;
--font-size-h1: 32px;
--font-size-body: 14px;

/* Spacing */
--spacing-xs: 4px;
--spacing-sm: 8px;
--spacing-md: 12px;
--spacing-lg: 16px;
--spacing-xl: 24px;
```

---

## 📚 Related Documentation

- **[PRODUCT_DESIGN_PRINCIPLES.md](PRODUCT_DESIGN_PRINCIPLES.md)** - Design methodologies and frameworks
- **[ASD_DESIGN_SYSTEM.md](ASD_DESIGN_SYSTEM.md)** - JSON format design system
- **[ASD_DESIGN_SYSTEM_GUIDE.md](ASD_DESIGN_SYSTEM_GUIDE.md)** - Figma implementation guide
- **[README.md](README.md)** - User guide and app documentation

---

**Last Updated**: January 2026  
**Version**: 3.0.17+81  
**Maintained By**: Absolute Stone Design Development Team
