# UI Components - Login Screen Style

This directory contains reusable UI components styled to match the Absolute Stone Design login screen.

## Components

### TextField

A text input component with label, icon support, and error handling, matching the login screen style.

**Features:**
- White background with rounded corners
- Left and right icon support
- Label text (uppercase styling)
- Error state display
- Gray placeholder text

**Props:**
- `label?: string` - Label text displayed above the field (automatically uppercase)
- `leftIcon?: React.ReactNode` - Icon displayed on the left side
- `rightIcon?: React.ReactNode` - Icon displayed on the right side
- `error?: string` - Error message to display below the field
- All standard `TextInput` props are supported

**Example:**
```tsx
import { TextField } from './components';
import { Ionicons } from '@expo/vector-icons';

<TextField
  label="Email"
  placeholder="Email"
  leftIcon={<Ionicons name="mail-outline" size={20} color="#000000" />}
  value={email}
  onChangeText={setEmail}
/>
```

### Button

A button component with primary and social variants, matching the login screen style.

**Features:**
- Primary button: Dark blue background with white border and underlined text
- Social button: White square background for social login buttons
- Loading state support
- Disabled state support

**Props:**
- `title: string` - Button text
- `onPress: () => void` - Press handler
- `variant?: 'primary' | 'social'` - Button style variant (default: 'primary')
- `disabled?: boolean` - Disable the button
- `loading?: boolean` - Show loading indicator
- `style?: ViewStyle` - Additional container styles
- `textStyle?: TextStyle` - Additional text styles

**Example:**
```tsx
import { Button } from './components';

// Primary button (like LOGIN button)
<Button
  title="LOGIN"
  onPress={handleLogin}
  variant="primary"
/>

// Social button (like Google/Apple login)
<Button
  title="G"
  onPress={handleGoogleLogin}
  variant="social"
/>
```

## Full Login Screen Example

See `LoginExample.tsx` for a complete example of how to use these components together to create a login screen matching the design.

## Styling Notes

The components are styled to match the login screen design:
- **Text Fields**: White background (#FFFFFF), rounded corners (12px), 56px height
- **Primary Button**: Dark blue background (#1E3A5F), white border, underlined white text
- **Social Buttons**: White background, 56x56 square with rounded corners
- **Text Colors**: Labels are white (#FFFFFF), placeholder text is gray (#999)

## Dependencies

These components require:
- React Native (or React Native Web)
- Icon library (e.g., @expo/vector-icons, react-native-vector-icons)
- React Native's StyleSheet API

Adjust imports based on your specific icon library and platform setup.
