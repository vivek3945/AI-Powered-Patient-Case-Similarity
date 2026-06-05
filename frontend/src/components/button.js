import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cn } from "./utils"; // Utility to combine class names
import './button.css'; // Import the CSS file for Button styles

const buttonVariants = {
  default: 'button-default button-default-size',
  destructive: 'button-destructive',
  outline: 'button-outline',
  secondary: 'button-secondary',
  ghost: 'button-ghost',
  link: 'button-link',
};

const buttonSizes = {
  default: 'button-default-size',
  sm: 'button-sm',
  lg: 'button-lg',
  icon: 'button-icon',
};

const Button = React.forwardRef(
  ({ className, variant = 'default', size = 'default', asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";
    
    const variantClass = buttonVariants[variant] || buttonVariants.default;
    const sizeClass = buttonSizes[size] || buttonSizes.default;
    
    return (
      <Comp
        className={cn(`${variantClass} ${sizeClass} ${className}`)}
        ref={ref}
        {...props}
      />
    );
  }
);

Button.displayName = "Button";

export { Button, buttonVariants };
