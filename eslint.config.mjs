import js from "@eslint/js";
import globals from "globals";
import prettier from "eslint-config-prettier/flat";

export default [
  js.configs.recommended,
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "script",
      globals: {
        ...globals.node,
      },
    },
    ignores: ["node_modules/", "**/*.py", "**/*.sql", "**/*.rs"],
    rules: {
      eqeqeq: "error",
      "no-implicit-coercion": "warn",
      "no-shadow": "warn",
      "no-redeclare": "error",
      "no-var": "off",
      "prefer-const": "error",
      "no-unused-vars": "off", // ["warn", { argsIgnorePattern: "^_" }],
      "no-console": "warn",
    },
  },
  prettier,
];
