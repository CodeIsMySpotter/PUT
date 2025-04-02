#include <widget.h>

typedef enum {
  CONTAINER,    // Represents a container widget
  BUTTON,       // Represents a button widget
  TEXT,         // Represents a text widget
  ICON,         // Represents an image widget (icon)
} WidgetType;

/**
 * @brief Structure representing a container widget.
 *        Can be used to hold other widgets (children).
 */
typedef struct {
  int width, height;      ///< Width and height of the container
  int borderRadius;       ///< Border radius for rounded corners
} Container;

/**
 * @brief Structure representing a text widget.
 *        Displays a text string.
 */
typedef struct {
  int width, height;      ///< Width and height of the text widget
  int borderRadius;       ///< Border radius for rounded corners
  char text[50];          ///< Text content to be displayed
} Text;

/**
 * @brief Structure representing an image (icon) widget.
 *        Displays an image (icon).
 */
typedef struct {
  int width, height;      ///< Width and height of the image widget
  int borderRadius;       ///< Border radius for rounded corners
} Image;

/**
 * @brief Structure representing a button widget.
 *        A clickable widget that can trigger an action.
 */
typedef struct {
  int width, height;      ///< Width and height of the button
  int borderRadius;       ///< Border radius for rounded corners
} Button;

/**
 * @brief Structure representing a generic widget.
 *        This structure can hold different types of widgets (e.g., Container, Button, Text, Image).
 */
typedef struct {
  WidgetType type;        ///< Type of the widget (e.g., CONTAINER, BUTTON, TEXT, ICON)
  union {
    Container;            ///< Container widget
    Text;                 ///< Text widget
    Image;                ///< Image widget
    Button;               ///< Button widget
  };
  Widget** children;      ///< Pointer to an array of child widgets (for container widgets)
  int childrenCount;      ///< Number of children the widget has
} Widget;
