import React, { useState } from 'react';
import { View, StyleSheet, Alert, KeyboardAvoidingView, Platform, TouchableOpacity } from 'react-native';
import { TextField } from './TextField';
import { Button } from './Button';
import { Ionicons } from '@expo/vector-icons'; // Adjust import based on your icon library

/**
 * Example usage of TextField and Button components styled like the login screen
 */
export const LoginExample: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);

  const handleLogin = () => {
    if (!email || !password) {
      Alert.alert('Error', 'Please fill in all fields');
      return;
    }
    Alert.alert('Success', 'Login successful!');
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    >
      <View style={styles.content}>
        {/* Email Field */}
        <TextField
          label="Email"
          placeholder="Email"
          value={email}
          onChangeText={setEmail}
          keyboardType="email-address"
          autoCapitalize="none"
          autoCorrect={false}
          leftIcon={
            <Ionicons name="mail-outline" size={20} color="#000000" />
          }
        />

        {/* Password Field */}
        <TextField
          label="Password"
          placeholder="Your Password"
          value={password}
          onChangeText={setPassword}
          secureTextEntry={!showPassword}
          leftIcon={
            <Ionicons name="lock-closed-outline" size={20} color="#000000" />
          }
          rightIcon={
            <TouchableOpacity onPress={() => setShowPassword(!showPassword)}>
              <Ionicons
                name={showPassword ? 'eye-outline' : 'eye-off-outline'}
                size={20}
                color="#000000"
              />
            </TouchableOpacity>
          }
        />

        {/* Login Button */}
        <Button
          title="LOGIN"
          onPress={handleLogin}
          variant="primary"
          style={styles.loginButton}
        />

        {/* Social Login Buttons */}
        <View style={styles.socialButtonsContainer}>
          <Button
            title="G"
            onPress={() => Alert.alert('Google Login', 'Google sign in pressed')}
            variant="social"
          />
          <View style={styles.socialButtonSpacer} />
          <Button
            title="🍎"
            onPress={() => Alert.alert('Apple Login', 'Apple sign in pressed')}
            variant="social"
          />
        </View>
      </View>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0D1B2A', // Dark blue gradient background (adjust as needed)
  },
  content: {
    padding: 20,
    flex: 1,
    justifyContent: 'center',
  },
  loginButton: {
    marginTop: 20,
    marginBottom: 20,
  },
  socialButtonsContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  socialButtonSpacer: {
    width: 16,
  },
});
