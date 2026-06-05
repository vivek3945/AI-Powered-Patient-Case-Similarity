import * as React from "react";
import { cn } from "./utils";
import './input.css'
const Input = React.forwardRef(({ className, type, ...props }, ref) => {
  return (
    <input
      type={type}
      className={cn(
        "input-base",  // Applying the base input styles
        className // Allow for external customization
      )}
      ref={ref}
      {...props}
    />
  );
});
Input.displayName = "Input";

export { Input };
