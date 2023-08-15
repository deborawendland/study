package factory;

import factory.service.ShapeFactory;

public class App {

    public static void main(String[] args) {
        ShapeFactory shapeFactory = new ShapeFactory();
        shapeFactory.getShape("circle").draw();
        shapeFactory.getShape("square").draw();
        shapeFactory.getShape("triangle").draw();
    }
}
