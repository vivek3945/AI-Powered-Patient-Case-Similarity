/**
 * Utility function to conditionally join class names.
 * @param  {...any} classes - Class names to join.
 * @returns {string} - A string of joined class names.
 */
export function cn(...classes) {
    return classes.filter(Boolean).join(" ");
  }
  