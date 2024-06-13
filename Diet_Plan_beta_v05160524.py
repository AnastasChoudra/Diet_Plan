from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.button import MDRaisedButton

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)

    MDDropDownItem:
        id: lunch_combo
        text: 'Select Lunch'
        on_release: app.menu_lunch.open()
    
    CheckBox:
        id: lunch_double
        size_hint: None, None
        size: dp(48), dp(48)
        active: False
        on_active: app.update_display()

    MDDropDownItem:
        id: dinner_combo
        text: 'Select Dinner'
        on_release: app.menu_dinner.open()
    
    CheckBox:
        id: dinner_double
        size_hint: None, None
        size: dp(48), dp(48)
        active: False
        on_active: app.update_display()

    MDDropDownItem:
        id: snack_combo
        text: 'Select Snack'
        on_release: app.menu_snack.open()
    
    CheckBox:
        id: snack_double
        size_hint: None, None
        size: dp(48), dp(48)
        active: False
        on_active: app.update_display()

    MDLabel:
        id: total_calories
        text: 'Total Calories: 0 kcal'

    ScrollView:
        MDLabel:
            id: meal_details
            text: 'Meal Details'
            size_hint_y: None
            height: self.texture_size[1]
'''

class MealPlannerApp(MDApp):
    def build(self):
        self.meal_options = {
            'lunch': {
                "Turkey and Avocado Wrap": {
                "calories": 400,
                "details": "Slices of turkey breast, avocado (small portion - 1/4 avocado), tomatoes, and lettuce in a low-calorie whole wheat wrap. Spice as desired, low-calorie sauce is accepted."
                },
                "Salmon Salad": {
                    "calories": 550,
                    "details": "1 Salmon fillet with a salad of choice. Recommended: Greek Salad with tomato, cucumber, onion, optional peppers, feta cheese, and 1 tbsp extra virgin olive oil; or Green Leaf Salad with any greens like spinach or kale."
                },
                "Stuffed Pepper (Baked)": {
                    "calories": 350,
                    "details": "Bell pepper filled with a mixture of lean ground beef, brown rice (1/4 cup cooked), diced tomatoes, and spices, baked until tender."
                },
                "Chicken (Caesar) Salad": {
                    "calories": 400,
                    "details": "Grilled chicken breast, romaine lettuce, a sprinkle of parmesan, whole grain croutons, and light Caesar dressing. Can be modified into a non-Caesar version if required."
                },
                "Beef Stir-Fry with Brown Rice": {
                    "calories": 500,
                    "details": "Thinly sliced lean beef stir-fried with broccoli, bell peppers, or any other ingredient of choice, served over a small portion of brown or white rice (1/2 cup cooked)."
                },
                "Granola with Fruits": {
                    "calories": 450,
                    "details": "1/2 cup of granola with low-fat milk and slices of banana, berries, etc. Granola can be substituted for oats."
                },
                "Chicken and Vegetable Soup": {
                    "calories": 350,
                    "details": "Shredded chicken breast in vegetable broth with mixed vegetables (carrots, celery, zucchini, etc.)."
                },
                "Quinoa and Black Bean Bowl": {
                    "calories": 500,
                    "details": "1 cup of cooked quinoa, black (or any other) beans (1/2 cup), corn, diced tomatoes, and onions (cilantro) with a dressing of choice."
                }
            },
            'dinner': {
                "Grilled Herb Chicken with Roasted Vegetables": {
                "calories": 500,
                "details": "Grilled marinated chicken breast with roasted veggies of choice and one sweet potato, preferably after working out."
                },
                "Meatball Spaghetti": {
                    "calories": 600,
                    "details": "One serving of spaghetti (1 cup cooked) of choice in meatball sauce (3 medium-sized meatballs)."
                },
                "Pork Tenderloin and Green Beans": {
                    "calories": 450,
                    "details": "Roasted pork tenderloin with a side of steamed green beans. Brussels sprouts, asparagus, etc. can be used as substitutes."
                },
                "Shrimp and Vegetable Stir-Fry with Brown Rice": {
                    "calories": 400,
                    "details": "Stir-fried shrimp with broccoli, bell peppers, and carrots in a light soy sauce, served over brown rice (1/2 cup cooked)."
                },
                "Mushroom Stuffed Pepper with Feta": {
                    "calories": 300,
                    "details": "Baked bell pepper stuffed with a mixture of mushrooms, onions, spinach, and feta cheese."
                },
                "Beef Burgers with Sweet Potato Fries": {
                    "calories": 550,
                    "details": "Grilled skinny beef burgers (low cal, no bun) served with a side of baked sweet potato fries and a small green salad."
                },
                "Vegetable and Beef Stir-Fry": {
                    "calories": 450,
                    "details": "Stir-fried beef with a mix of snow peas, bell peppers, and carrots in a ginger soy sauce, served over a small serving of brown (or white) rice (1/2 cup cooked)."
                },
                "Salmon Pasta": {
                    "calories": 700,
                    "details": "Whole wheat (or normal) pasta (1 cup cooked) with grilled salmon, asparagus, and a light creamy sauce made from low-fat cream cheese and herbs. Consider adding spinach."
                }
            },
            'snack': {
                    "Mixed Nuts": {
                    "calories": 200,
                    "details": "A small handful of mixed nuts (almonds, walnuts, cashews)."
                },
                "Greek Yogurt with Honey": {
                    "calories": 250,
                    "details": "Non-fat Greek yogurt mixed with 1 tbsp of honey."
                },
                "Protein Shake": {
                    "calories": 400,
                    "details": "2 Scoops of Protein shake, with water or milk."
                },
                "Protein Smoothie": {
                    "calories": 500,
                    "details": "Protein shake made with protein powder, milk of choice, fruits of choice, 1 tbsp of peanut butter, and oats."
                },
                "Cottage Cheese": {
                    "calories": 250,
                    "details": "One Cup of low fat cottage cheese"
                },
                "Boiled Eggs": {
                    "calories": 150,
                    "details": "2 boiled eggs (or pan-fried but without Added Oil)"
                },
                "Fruit Bowl": {
                    "calories": 200,
                    "details": "Any fruit combination of choice"
                },
                "Air-popped Popcorn": {
                    "calories": 150,
                    "details": "Low calorie microwave popcorn"
                },
                "Dark chocolate": {
                    "calories": 200,
                    "details": "Minimum 70 per-cent dark chocolate (2 squares - 100g)"
                },
                "Greek Yogurt with berries": {
                    "calories": 250,
                    "details": "One Cup of low (or zero) fat Greek yogurt with berries of choice"
                },
                "Peanut Butter Banana Slices": {
                    "calories": 250,
                    "details": "Banana Slices topped with peanut butter"
                },
                "Dried Dates": {
                    "calories": 150,
                    "details": "Two Sweet Medjool Dates (or similar)"
                },
                "Fruit and Nut Trail Mix": {
                    "calories": 200,
                    "details": "Fruits and Nuts of choice (1 small bowl)"
                },
                "Protein Bar": {
                    "calories": 250,
                    "details": "Any protein bar of choice"
                },
                "Protein Pancakes": {
                    "calories": 400,
                    "details": "Pre-made protein Pancakes. Can be found on various supermarkets"
                },
                "Protein Mousse": {
                    "calories": 200,
                    "details": "Various flavours, can be found in major supermarkets"
                },
            }
        }
        return Builder.load_string(KV)

    def on_start(self):
        self.menu_lunch = self.create_menu('lunch')
        self.menu_dinner = self.create_menu('dinner')
        self.menu_snack = self.create_menu('snack')

    def create_menu(self, category):
        from kivymd.uix.menu import MDDropdownMenu
        items = [
            {
                "text": item,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=item: self.set_item(category, x)
            } for item in self.meal_options[category].keys()
        ]
        return MDDropdownMenu(
            caller=self.root.ids[f'{category}_combo'],
            items=items,
            width_mult=4,
        )

    def set_item(self, category, text_item):
        self.root.ids[f'{category}_combo'].set_item(text_item)
        self.update_display()

    def update_display(self):
        lunch_meal = self.root.ids.lunch_combo.current_item
        dinner_meal = self.root.ids.dinner_combo.current_item
        snack_meal = self.root.ids.snack_combo.current_item

        lunch_double = self.root.ids.lunch_double.active
        dinner_double = self.root.ids.dinner_double.active
        snack_double = self.root.ids.snack_double.active

        total_calories = 0
        details_text = ""

        if lunch_meal in self.meal_options['lunch']:
            calories = self.meal_options['lunch'][lunch_meal]['calories']
            total_calories += calories * (2 if lunch_double else 1)
            details_text += f"Lunch - {lunch_meal}: {self.meal_options['lunch'][lunch_meal]['details']}"
            if lunch_double:
                details_text += " (Double Portion)"
            details_text += "\n"
        
        if dinner_meal in self.meal_options['dinner']:
            calories = self.meal_options['dinner'][dinner_meal]['calories']
            total_calories += calories * (2 if dinner_double else 1)
            details_text += f"Dinner - {dinner_meal}: {self.meal_options['dinner'][dinner_meal]['details']}"
            if dinner_double:
                details_text += " (Double Portion)"
            details_text += "\n"
        
        if snack_meal in self.meal_options['snack']:
            calories = self.meal_options['snack'][snack_meal]['calories']
            total_calories += calories * (2 if snack_double else 1)
            details_text += f"Snack - {snack_meal}: {self.meal_options['snack'][snack_meal]['details']}"
            if snack_double:
                details_text += " (Double Portion)"
            details_text += "\n"

        self.root.ids.total_calories.text = f'Total Calories: {total_calories} kcal'
        self.root.ids.meal_details.text = details_text

if __name__ == "__main__":
    MealPlannerApp().run()